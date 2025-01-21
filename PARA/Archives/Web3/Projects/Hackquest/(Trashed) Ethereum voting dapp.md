
# Building an Ethereum Voting DApp with Hardhat and Next.js

As a beginner familiar with Solana and Rust, transitioning to Ethereum and Solidity might seem challenging. However, with the right tools and step-by-step guidance, you can successfully build and deploy a decentralized voting application (DApp) for the Mantle APAC Hackathon. This guide will walk you through the entire process using **Hardhat** for smart contract development and **Next.js** for the frontend.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Project Setup](#project-setup)
3. [Smart Contract Development with Hardhat](#smart-contract-development-with-hardhat)
    - [1. Initialize Hardhat Project](#1-initialize-hardhat-project)
	- [2. Develop the Voting Contract](#2-develop-the-voting-contract)
    - [3. Write Tests](#3-write-tests)
    - [4. Deploy the Contract](#4-deploy-the-contract)
4. [Frontend Development with Next.js](#frontend-development-with-nextjs)
    - [1. Initialize Next.js Project](#1-initialize-nextjs-project)
    - [2. Install Dependencies](#2-install-dependencies)
    - [3. Configure Ethers.js](#3-configure-ethersjs)
    - [4. Create Voting Interface](#4-create-voting-interface)
5. [Connecting Frontend with Smart Contract](#connecting-frontend-with-smart-contract)
6. [Deploying to a Testnet](#deploying-to-a-testnet)
7. [Final Steps](#final-steps)
8. [Conclusion](#conclusion)

---

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- **Node.js** (v16 or later): [Download Node.js](https://nodejs.org/)
- **Yarn** or **npm**
- **Git**
- **MetaMask** extension installed in your browser

---

## Project Setup

Create a new directory for your project and navigate into it:

```bash
mkdir ethereum-voting-dapp
cd ethereum-voting-dapp
```

---

## Smart Contract Development with Hardhat

### 1. Initialize Hardhat Project

Initialize a new Hardhat project to manage your smart contracts.

```bash
# Initialize npm
yarn init -y

# Install Hardhat
yarn add --dev hardhat

# Initialize Hardhat
npx hardhat
```

When prompted, select **"Create a basic sample project"** and follow the instructions.

### 2. Develop the Voting Contract

Create a Solidity smart contract for voting.

#### `contracts/Voting.sol`

```solidity:contracts/Voting.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract Voting {
    struct Proposal {
        string name;
        uint voteCount;
    }

    address public owner;
    Proposal[] public proposals;
    mapping(address => bool) public hasVoted;

    event VoteCast(address voter, uint proposal);

    constructor(string[] memory proposalNames) {
        owner = msg.sender;
        for (uint i = 0; i < proposalNames.length; i++) {
            proposals.push(Proposal({name: proposalNames[i], voteCount: 0}));
        }
    }

    function vote(uint proposalIndex) public {
        require(!hasVoted[msg.sender], "You have already voted.");
        require(proposalIndex < proposals.length, "Invalid proposal.");
        
        hasVoted[msg.sender] = true;
        proposals[proposalIndex].voteCount += 1;

        emit VoteCast(msg.sender, proposalIndex);
    }

    function getProposals() public view returns (Proposal[] memory) {
        return proposals;
    }
}
```

### 3. Write Tests

Ensure your smart contract works as expected by writing tests.

#### `test/Voting.js`

```javascript:test/Voting.js
const { expect } = require("chai");

describe("Voting Contract", function () {
  let Voting, voting, owner, addr1, addr2;

  beforeEach(async function () {
    Voting = await ethers.getContractFactory("Voting");
    voting = await Voting.deploy(["Proposal 1", "Proposal 2"]);
    await voting.deployed();

    [owner, addr1, addr2, _] = await ethers.getSigners();
  });

  it("Should initialize with correct proposals", async function () {
    const proposals = await voting.getProposals();
    expect(proposals.length).to.equal(2);
    expect(proposals[0].name).to.equal("Proposal 1");
    expect(proposals[1].name).to.equal("Proposal 2");
  });

  it("Should allow a user to vote", async function () {
    await voting.connect(addr1).vote(0);
    const proposals = await voting.getProposals();
    expect(proposals[0].voteCount).to.equal(1);
    expect(await voting.hasVoted(addr1.address)).to.be.true;
  });

  it("Should prevent double voting", async function () {
    await voting.connect(addr1).vote(0);
    await expect(voting.connect(addr1).vote(1)).to.be.revertedWith("You have already voted.");
  });

  it("Should prevent voting for non-existent proposal", async function () {
    await expect(voting.connect(addr1).vote(5)).to.be.revertedWith("Invalid proposal.");
  });
});
```

Run the tests:

```bash
npx hardhat test
```

### 4. Deploy the Contract

Create a deployment script to deploy your contract to a local network.

#### `scripts/deploy.js`

```javascript:scripts/deploy.js
const hre = require("hardhat");

async function main() {
  const proposals = ["Proposal 1", "Proposal 2", "Proposal 3"];
  const Voting = await hre.ethers.getContractFactory("Voting");
  const voting = await Voting.deploy(proposals);

  await voting.deployed();

  console.log("Voting deployed to:", voting.address);
}

main()
  .then(() => process.exit(0))
  .catch(error => {
    console.error(error);
    process.exit(1);
  });
```

Start a local Hardhat node:

```bash
npx hardhat node
```

In a new terminal, deploy the contract:

```bash
npx hardhat run scripts/deploy.js --network localhost
```

Note the deployed contract address for frontend integration.

---

## Frontend Development with Next.js

### 1. Initialize Next.js Project

Navigate back to the root directory and create the Next.js app.

```bash
cd ..
npx create-next-app frontend
cd frontend
```

### 2. Install Dependencies

Install necessary packages for interacting with Ethereum.

```bash
yarn add ethers
yarn add --dev typescript @types/node @types/react
```

Initialize TypeScript:

```bash
touch tsconfig.json
yarn add --dev @types/react
```

### 3. Configure Ethers.js

Set up Ethers.js to interact with your smart contract.

#### `utils/contract.ts`

```typescript:frontend/utils/contract.ts
import { ethers } from "ethers";
import Voting from "../artifacts/contracts/Voting.sol/Voting.json";

const contractAddress = "YOUR_DEPLOYED_CONTRACT_ADDRESS";

export const getContract = (signer: ethers.Signer) => {
  return new ethers.Contract(contractAddress, Voting.abi, signer);
};
```

Replace `YOUR_DEPLOYED_CONTRACT_ADDRESS` with the address from the deployment step.

### 4. Create Voting Interface

Build a simple UI for voting.

#### `pages/index.tsx`

```typescript:frontend/pages/index.tsx
import { useEffect, useState } from "react";
import { ethers } from "ethers";
import { getContract } from "../utils/contract";
import Head from "next/head";

const Home = () => {
  const [proposals, setProposals] = useState<any[]>([]);
  const [account, setAccount] = useState<string>("");
  const [loading, setLoading] = useState<boolean>(false);

  useEffect(() => {
    if (typeof window.ethereum !== "undefined") {
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const signer = provider.getSigner();
      const contract = getContract(signer);

      contract.getProposals().then((proposals: any[]) => {
        setProposals(proposals);
      });

      provider.listAccounts().then((accounts) => {
        if (accounts.length > 0) setAccount(accounts[0]);
      });
    }
  }, []);

  const connectWallet = async () => {
    if (!window.ethereum) return;
    const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
    setAccount(accounts[0]);
  };

  const castVote = async (index: number) => {
    if (!account) return;
    setLoading(true);
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const signer = provider.getSigner();
    const contract = getContract(signer);
    try {
      const tx = await contract.vote(index);
      await tx.wait();
      const updatedProposals = await contract.getProposals();
      setProposals(updatedProposals);
      alert("Vote cast successfully!");
    } catch (error) {
      console.error(error);
      alert("Error casting vote.");
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100">
      <Head>
        <title>Ethereum Voting DApp</title>
      </Head>

      <h1 className="text-4xl font-bold mb-6">Ethereum Voting DApp</h1>

      {!account ? (
        <button
          onClick={connectWallet}
          className="px-4 py-2 bg-blue-500 text-white rounded"
        >
          Connect Wallet
        </button>
      ) : (
        <p className="mb-4">Connected as: {account}</p>
      )}

      <div className="w-1/2">
        {proposals.map((proposal, index) => (
          <div key={index} className="flex justify-between items-center mb-2 p-2 bg-white rounded shadow">
            <span>{proposal.name}</span>
            <div>
              <span className="mr-4">Votes: {proposal.voteCount.toString()}</span>
              <button
                onClick={() => castVote(index)}
                className="px-3 py-1 bg-green-500 text-white rounded"
                disabled={loading}
              >
                Vote
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Home;
```

### 5. Add Tailwind CSS for Styling

Enhance the UI with Tailwind CSS.

```bash
yarn add -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

#### `tailwind.config.js`

```javascript:frontend/tailwind.config.js
module.exports = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
```

#### `styles/globals.css`

```css:frontend/styles/globals.css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

---

## Connecting Frontend with Smart Contract

Ensure your frontend can communicate with the deployed smart contract.

1. **Start the Local Hardhat Node:**

   ```bash
   npx hardhat node
   ```

2. **Deploy the Contract:**

   ```bash
   npx hardhat run scripts/deploy.js --network localhost
   ```

3. **Update `contract.ts`:**

   Replace `contractAddress` with the deployed address.

4. **Start the Frontend:**

   ```bash
   yarn dev
   ```

5. **Connect MetaMask to Localhost:**

   - Open MetaMask.
   - Add a new network:
     - **Network Name:** Localhost 8545
     - **RPC URL:** http://localhost:8545
     - **Chain ID:** 31337
   - Import an account using the private key from Hardhat's local node.

---

## Deploying to a Testnet

Once satisfied with local testing, deploy your contract to an Ethereum testnet like Goerli.

### 1. Configure Hardhat for Testnet

#### `hardhat.config.js`

```javascript:hardhat.config.js
require("@nomiclabs/hardhat-waffle");

const INFURA_PROJECT_ID = "YOUR_INFURA_PROJECT_ID";
const PRIVATE_KEY = "YOUR_METAMASK_PRIVATE_KEY";

module.exports = {
  solidity: "0.8.17",
  networks: {
    goerli: {
      url: `https://goerli.infura.io/v3/${INFURA_PROJECT_ID}`,
      accounts: [PRIVATE_KEY],
    },
  },
};
```

Replace `YOUR_INFURA_PROJECT_ID` and `YOUR_METAMASK_PRIVATE_KEY` with your credentials.

### 2. Deploy to Goerli

```bash
npx hardhat run scripts/deploy.js --network goerli
```

Note the deployed contract address for frontend integration.

### 3. Update Frontend Configuration

Replace the `contractAddress` in `utils/contract.ts` with the Goerli deployment address.

---

## Final Steps

1. **Test the DApp on Testnet:**
   - Connect MetaMask to Goerli.
   - Interact with the voting interface to ensure functionality.

2. **Prepare Submission:**
   - Ensure your code is well-documented.
   - Create a README with setup instructions.
   - Record a demo video showcasing your DApp.
   - Push your code to GitHub.

3. **Share on Social Media:**
   - Post about your project on X (formerly Twitter) and tag `@0xMantleDevs`.

---

## Conclusion

You've successfully built and deployed an Ethereum-based Voting DApp using Hardhat and Next.js. This foundational project not only enhances your understanding of Solidity and Ethereum development but also positions you well for the Mantle APAC Hackathon. As you progress, consider adding more features like user authentication, proposal creation by users, and real-time vote tracking to make your DApp more robust and feature-rich.

---

**Good luck with the hackathon! 🚀**

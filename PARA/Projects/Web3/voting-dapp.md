
# Building a Voting DApp with Anchor and Next.js

Creating a voting decentralized application (DApp) on Solana using Anchor and Next.js involves several steps. Here's a comprehensive guide to help you get started as a beginner in Web3.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js (v16 or later)**
- **Yarn** or **npm**
- **Rust** and **Cargo**
- **Solana CLI**
- **Anchor CLI**

### Install Node.js and Yarn

```bash
# Install Node.js from https://nodejs.org/
# Then install Yarn
npm install --global yarn
```

### Install Rust and Cargo

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

### Install Solana CLI

```bash
sh -c "$(curl -sSfL https://release.solana.com/v1.14.11/install)"
```

### Install Anchor CLI

```bash
cargo install --git https://github.com/project-serum/anchor anchor-cli --locked
```

## Step 1: Initialize the Project

Use `npx create-solana-dapp` to scaffold your project.

```bash
npx create-solana-dapp voting-dapp
cd voting-dapp
yarn install
```

## Step 2: Set Up Anchor

Initialize Anchor in your project.

```bash
anchor init voting
cd voting
```

### Update `Anchor.toml`

Ensure your `Anchor.toml` is configured correctly for your workspace.

```toml
[workspace]
members = [
  "programs/voting",
  "tests/voting"
]
```

## Step 3: Develop the Smart Contract

Create the voting program using Anchor.

### `programs/voting/src/lib.rs`

```rust:programs/voting/src/lib.rs
use anchor_lang::prelude::*;

declare_id!("YourProgramID");

#[program]
pub mod voting {
    use super::*;
    pub fn initialize(ctx: Context<Initialize>) -> ProgramResult {
        let base_account = &mut ctx.accounts.base_account;
        base_account.total_votes = 0;
        Ok(())
    }

    pub fn cast_vote(ctx: Context<CastVote>) -> ProgramResult {
        let base_account = &mut ctx.accounts.base_account;
        base_account.total_votes += 1;
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub base_account: Account<'info, BaseAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program <'info, System>,
}

#[derive(Accounts)]
pub struct CastVote<'info> {
    #[account(mut)]
    pub base_account: Account<'info, BaseAccount>,
}

#[account]
pub struct BaseAccount {
    pub total_votes: u64,
}
```

## Step 4: Build and Deploy the Smart Contract

Build the Anchor program.

```bash
anchor build
```

Deploy to the local Solana cluster.

```bash
solana-test-validator
```

In a new terminal:

```bash
anchor deploy
```

## Step 5: Develop the Frontend with Next.js

Navigate to the frontend directory and initialize Next.js.

```bash
cd ../app
yarn create next-app@latest .
```

### Install Dependencies

```bash
yarn add @solana/web3.js @project-serum/anchor react
```

### Create Solana Context

#### `app/context/SolanaContext.tsx`

```typescript:app/context/SolanaContext.tsx
import { createContext, useContext } from 'react';
import { Connection, PublicKey } from '@solana/web3.js';
import { Program, AnchorProvider, web3 } from '@project-serum/anchor';
import idl from '../../target/idl/voting.json';

const { SystemProgram } = web3;

const network = 'http://localhost:8899';
const opts = {
  preflightCommitment: 'processed',
};

const SolanaContext = createContext(null);

export const SolanaProvider: React.FC = ({ children }) => {
  const connection = new Connection(network, opts.preflightCommitment);
  const provider = new AnchorProvider(connection, window.solana, opts.preflightCommitment);
  const programID = new PublicKey(idl.metadata.address);
  const program = new Program(idl, programID, provider);

  return (
    <SolanaContext.Provider value={{ connection, provider, program }}>
      {children}
    </SolanaContext.Provider>
  );
};

export const useSolana = () => useContext(SolanaContext);
```

## Step 6: Implement Voting Functionality

### Create Voting Component

#### `app/components/VoteButton.tsx`

```typescript:app/components/VoteButton.tsx
import React, { useState } from 'react';
import { useSolana } from '../context/SolanaContext';

const VoteButton: React.FC = () => {
  const { program } = useSolana();
  const [isLoading, setIsLoading] = useState(false);
  const [totalVotes, setTotalVotes] = useState<number | null>(null);

  const castVote = async () => {
    setIsLoading(true);
    try {
      const baseAccount = await program.account.baseAccount.fetch(/* PublicKey */);
      await program.rpc.castVote({
        accounts: {
          baseAccount: baseAccount.publicKey,
        },
      });
      setTotalVotes(baseAccount.totalVotes.toNumber() + 1);
    } catch (error) {
      console.error('Error casting vote:', error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div>
      <button
        onClick={castVote}
        disabled={isLoading}
        className="px-4 py-2 bg-blue-500 text-white rounded"
      >
        {isLoading ? 'Voting...' : 'Cast Vote'}
      </button>
      {totalVotes !== null && <p>Total Votes: {totalVotes}</p>}
    </div>
  );
};

export default VoteButton;
```

## Step 7: Integrate Components into Pages

### Update `_app.tsx`

#### `app/pages/_app.tsx`

```typescript:app/pages/_app.tsx
import '../styles/globals.css';
import type { AppProps } from 'next/app';
import { SolanaProvider } from '../context/SolanaContext';

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <SolanaProvider>
      <Component {...pageProps} />
    </SolanaProvider>
  );
}

export default MyApp;
```

### Create Home Page

#### `app/pages/index.tsx`

```typescript:app/pages/index.tsx
import type { NextPage } from 'next';
import Head from 'next/head';
import VoteButton from '../components/VoteButton';

const Home: NextPage = () => {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen py-2">
      <Head>
        <title>Voting DApp</title>
        <meta name="description" content="Decentralized Voting Application" />
      </Head>

      <main className="flex flex-col items-center justify-center w-full flex-1 px-20 text-center">
        <h1 className="text-4xl font-bold">Welcome to the Voting DApp</h1>
        <VoteButton />
      </main>
    </div>
  );
};

export default Home;
```

## Step 8: Run the Application

Start the Next.js development server.

```bash
yarn dev
```

Open [http://localhost:3000](http://localhost:3000) to view your DApp.

## Conclusion

You've successfully set up a basic voting DApp on Solana using Anchor and Next.js. From here, you can expand functionality, enhance the UI with Tailwind CSS or Shadcn UI, and implement additional features such as user authentication and multiple voting options.

---

For further learning, consider exploring:

- **Anchor Documentation:** [https://project-serum.github.io/anchor/](https://project-serum.github.io/anchor/)
- **Solana Web3.js:** [https://solana-labs.github.io/solana-web3.js/](https://solana-labs.github.io/solana-web3.js/)
- **Next.js Documentation:** [https://nextjs.org/docs](https://nextjs.org/docs)

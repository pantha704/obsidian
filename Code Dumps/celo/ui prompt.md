
## 🚀 Complete Celo Earn dApp Development Prompt

**Project:** celo-earn - Decentralized Bounty Platform on Celo  
**Goal:** Create a fully functional dApp where anyone can create micro-bounties and earn cUSD

### 📋 **Core Requirements**

**Blockchain Setup:**
- Use Celo SDK with Alfajores testnet
- Contract Address: `0x540d7E428D5207B30EE03F2551Cbb5751D3c7569`
- cUSD Address: `0x874069Fa1Eb16D44d622F2e0Ca25eeA172369bC1`
- ABI: [Full ABI from constants.ts]

**Key Features:**
1. **Landing Page** - Professional, mobile-first design with clear value proposition
2. **Bounty Marketplace** - Browse, accept, and complete tasks
3. **Bounty Creation** - Simple form to create new bounties
4. **User Dashboard** - Personal task management
5. **Admin Panel** - Platform management (owner-only)

### 🎨 **UI/UX Specifications**

**Design Theme:**
- **Primary Colors:** Green (#10B981) and white clean theme
- **Vibe:** Professional, trustworthy, Web3-native
- **Mobile-first** responsive design
- **Consistent** navigation and branding throughout

**Landing Page Sections:**
1. **Hero Section:** "Earn cUSD by Completing Tasks" with two CTAs:
   - "Create Bounty" (leads to bounty creation)
   - "Browse Bounties" (leads to marketplace)
2. **Value Proposition:** "Decentralized, mobile-first, carbon-negative bounties"
3. **How It Works:** 4-step visual workflow
4. **Stats:** Platform metrics (total bounties, paid out, etc.)

### 📱 **Page Flows & Functionality**

#### **1. Bounty Marketplace (`/bounties`)**
- **Display:** Grid/list of all available bounties from `getTasks()`
- **Filters:** Open bounties, in-progress, completed
- **Bounty Card Components:**
  - Title, description, reward amount
  - Status badge (Open/In Progress/Completed/Paid)
  - Creator/worker addresses (truncated)
  - Action buttons (Accept/Submit Proof/Release Payment)
  - **Accept Flow:** Wallet connection → acceptTask() call
  - **Submit Proof:** Modal with IPFS/URL input → submitProof()

#### **2. Bounty Creation (`/create-bounty`)**
- **Form Fields:** Title (text), Description (textarea), Reward (number in cUSD)
- **Validation:** Non-empty fields, minimum reward > 0
- **Submission Flow:**
  1. Check cUSD allowance → request approval if needed
  2. Convert decimal reward to wei (18 decimals)
  3. Call `createTask()` with parameters
  4. Success confirmation with task ID

#### **3. User Dashboard (`/dashboard`)**
**For Regular Users:**
- **Created Bounties:** List of bounties user created
  - View submissions for each bounty
  - Release payment to selected worker
- **Accepted Bounties:** Bounties user is working on
  - Submit proof functionality
- **Transaction History:** All user interactions
- **Wallet Balance:** cUSD and CELO balances

**For Contract Owner (Admin):**
- **Admin Panel:** Access to `setPlatformFee`, `setPlatformWallet`, `withdrawStuckTokens`
- **Platform Stats:** Total fees collected, active bounties

#### **4. Task Management System**
**Creator View:**
- "Your Bounties" section with:
  - Pending submissions for each bounty
  - Ability to view proofs and release payment to specific workers
  - Cancel unaccepted bounties

**Worker View:**
- "Your Tasks" section with:
  - Active bounties needing proof submission
  - Completed tasks awaiting payment
  - Payment history

### 🔗 **Smart Contract Integration**

**Required Contract Calls:**
- `getTasks()` - Fetch all bounties
- `createTask(title, description, reward)` - Create new bounty
- `acceptTask(id)` - Accept a bounty
- `submitProof(id, proof)` - Submit work proof
- `releasePayment(id)` - Release payment to worker
- `cancelTask(id)` - Cancel unaccepted bounty
- `getTaskCount()` - Get total bounties
- `calculateFee(amount)` - Show fee breakdown

**Wallet Integration:**
- Celo-compatible wallet connection (Valora, MetaMask)
- cUSD balance checking and approval flows
- Transaction status tracking

### 🎯 **User Experience Flows**

**Complete Bounty Flow:**
1. User connects wallet → browses bounties
2. Clicks "Accept" → transaction confirmation
3. Completes work → submits proof via modal
4. Creator reviews → releases payment
5. Worker receives 93% (7% platform fee)

**Create Bounty Flow:**
1. User clicks "Create Bounty" → fills form
2. Approves cUSD spending → creates bounty
3. Bounty appears in marketplace
4. Manages submissions and payments

### 📊 **Data Display & States**

**Bounty Status Indicators:**
- 🟢 **Open:** No worker assigned
- 🔵 **In Progress:** Worker assigned, no proof
- 🟡 **Pending Payment:** Proof submitted, unpaid
- 🟣 **Paid:** Reward released

**Real-time Updates:**
- Auto-refresh bounty list every 30 seconds
- Event listeners for contract events
- Wallet balance updates

### 🛠 **Technical Specifications**

**Tech Stack:**
- **Framework:** Next.js 14+ with TypeScript
- **Blockchain:** Celo SDK + ethers.js
- **Styling:** Tailwind CSS with custom components
- **State Management:** React Context or Zustand
- **Wallet:** ThirdWeb or RainbowKit for Celo

**File Structure:**
```
/app
  /bounties - Marketplace
  /create - Bounty creation
  /dashboard - User dashboard
  /admin - Admin panel (owner-only)
/components
  /bounty - Bounty cards, creation forms
  /wallet - Connection, balance display
/lib
  /celo - Contract interactions, constants
```

### 🎉 **Success Metrics**
- Seamless wallet connection and transaction flows
- Clear bounty status tracking for all parties
- Mobile-responsive design that works on Valora browser
- Professional appearance that builds trust
- Real-time updates without page refreshes

**Target Audience:** Individuals looking for micro-tasks, freelancers, DAO contributors, and bounty hunters in the Celo ecosystem.


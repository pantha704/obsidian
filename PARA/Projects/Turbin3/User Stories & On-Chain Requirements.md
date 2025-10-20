
# Assignment 2: Translating Strategy into a Proof-of-Concept (POC) Plan

## 1. Overview & Purpose

The goal of this assignment is to translate the strategic foundation from **Assignment 1** into an actionable plan for a **Proof-of-Concept (POC)**.  
You will define the key users of your proposed project, map their critical interactions, and derive the high-level on-chain requirements for the underlying smart contract architecture.  

This process creates the direct link between **user needs** and the **on-chain logic** that will be fully designed and diagrammed in the subsequent assignment.

---

## 2. Learning Objectives

- Identify and prioritize core user personas for a new product concept.  
- Map critical user functions and stories required to deliver value.  
- Refine user stories to be granular, clear, and action-oriented.  
- Translate user stories into specific, high-level on-chain requirements.  
- Define the core logic, state, and dependencies for smart contracts before architectural design.  
- Ensure alignment between high-level strategy and low-level technical planning.

---

## 3. Assignment Instructions

You will use the refined **Project Proposal from Assignment 1** as input for this assignment.  
As before, you must meticulously document your process in a **Process Appendix**.

---

## Part A: Initial User & Function Mapping

### 1) Manual User Brainstorming

**Task:**  
Based on your refined Value Proposition from Assignment 1, brainstorm a broad list of every potential user type who might interact with your project.

**Consider these categories:**
- **Direct Users:** Who will use the product day-to-day? (e.g., content creators, voters, investors)  
- **Indirect Users/Beneficiaries:** Who benefits from the direct users' actions? (e.g., content consumers, project owners)  
- **Administrators/Moderators:** Who will manage the system? (e.g., you as the developer, community moderators)  
- **Stakeholders:** Who has a vested interest in the project's success but may not use it directly? (e.g., token holders, partners)

**Output:**  
A preliminary, comprehensive list of all potential user types.

---

### 2) AI-Assisted User Prioritization

**AI Prompt:**  
> "My project's value proposition is [summarize from Assignment 1].  
> Here is a brainstormed list of all potential user types: [Paste your entire list from Step 1].  
> Based on the value proposition, which 2–5 of these user types are the most critical to focus on for an initial Proof-of-Concept?  
> For each user you recommend, provide a brief rationale explaining why they are essential for proving the project's core value."

**Manual Action & Output:**  
- Analyze the AI's recommendations and rationale.  
- Decide on your final prioritized list of **2–5 key user types.**  
- Document your final list and your decision-making process — where you agreed or disagreed with the AI and why.

---

### 3) Core Function Mapping

**AI Prompt:**  
> "For a project with this value proposition [summarize] and focusing on these prioritized user types [list your final selected types from Step 2],  
> help map out the key functions or interactions each user would need to perform."

**Output:**  
A list of key functions and interactions mapped to your prioritized user types.

---

### 4) Deriving Core POC Requirements

**Manual Task:**  
From the function map you just created, identify the **top 1–2 most critical user stories or interaction paths** essential for a POC.

**AI Prompt:**  
> "Based on these top 1–2 critical user interactions [describe interactions], what are the key technical requirements needed to build a proof-of-concept?"

**Output:**  
An initial list of key technical requirements derived from the core user interactions.

---

## Part B: Adversarial Analysis & Granularity Check

### 1) Critique & Refine User Stories / Requirements

**AI Prompt:**  
> "Review my core user functions/stories [Input from Part A, Step 3] and requirements [Input from Part A, Step 4].  
> Considering my project's refined value proposition [summarize from Assignment 1], do these stories truly hit the mark?  
> Are the requirements granular enough to map to specific technical components (e.g., database schemas, API endpoints, specific blockchain programs)?  
> What's missing or unclear?"

**Action:**  
- Analyze the AI feedback.  
- Refine your user stories for better alignment.  
- Ensure your technical requirements meet the **necessary granularity** for technical planning.

**Documentation:**  
Include:
- AI critique  
- Your analysis  
- Rationale for refinements made to user stories and technical requirements

---

## Part C: Granularity & Clarity Refinement

### 1) Final Manual Review & Refinement

**Goal:**  
Simplify and clarify every user story and function, preparing for technical implementation.

**Checklist:**
- **De-Jargon:**  
  Is the language free of technical jargon? Rewrite for a non-technical reader.
- **Granularity:**  
  Does each story represent a single, concrete action?
- **Atomicity:**  
  Break down any story that involves multiple distinct steps.
  - Example:  
    - ❌ “User signs up and creates a profile.”  
    - ✅ “Story 1: User signs up for an account.”  
      “Story 2: User fills out profile information.”
- **Clarity of Action:**  
  Is the action and desired outcome completely clear?
- **No Overlap:**  
  Merge or remove redundant stories.

**Documentation:**  
Create a **“Part C Refinement Log”** in your appendix.  
For each change:
- **Before:** Original story  
- **After:** Revised story  
- **Rationale:** e.g., “Split into two stories for atomicity,” “Removed jargon,” etc.

---

## Part D: Defining Potential On-Chain Requirements

### 1) Brainstorming On-Chain Requirements for Each User Story

**Task:**  
Take your final, refined list of user stories from Part C.  
For each story, create a bulleted list of **potential on-chain requirements** needed to make it happen.

**Example:**

#### User Story: “User creates a new project campaign.”

**Potential On-Chain Requirements:**
- Create a new on-chain account to hold campaign data  
- Store the campaign creator’s address for permissions  
- Include fundraising goal and deadline  
- Initialize a “total raised” amount to zero  

---

#### User Story: “User contributes funds to a campaign.”

**Potential On-Chain Requirements:**
- Function to accept a SOL transfer from the user  
- Funds sent to an account controlled by the campaign  
- Update the “total raised” field with the new amount  
- Fail the transaction if the campaign deadline has passed  

**Output:**  
A list of user stories, each followed by potential on-chain requirements.

---

## 4. Final Deliverable

Submit a single **PDF document** containing two parts:

### **Part A: User Stories & On-Chain Requirements Document**
- Final, clean versions of:
  - Core User Personas  
  - Function Maps  
  - Potential On-Chain Requirements (from Part D)

### **Part B: Process Appendix**
- Detailed log of your process, including:
  - Prompts  
  - AI outputs  
  - Analyses  
  - Rationale for all refinements from Parts A–D

---

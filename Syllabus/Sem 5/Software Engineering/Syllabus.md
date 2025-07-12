
### Ultimate Software Engineering Exam Cheat Sheet

---

#### **Module-I: SDLC Models [9L]**
* **Core Mechanics:**
  - **Waterfall Model:** Linear sequence (Requirements → Design → Code → Test → Maintain) like building a house with no design changes after blueprint sign-off.
  - **Spiral Model:** Risk-driven cycles (Plan → Risk Analysis → Develop → Evaluate) like software "evolution" through prototypes.
  - **COCOMO Model:** Estimates effort: `Effort = a * (KLOC)^b` (e.g., 2.4 * 50^1.05 = 135 person-months for 50K lines).

* **Key Comparisons:**
  | Model     | Flexibility | Risk Handling | Best For          |
  |-----------|-------------|---------------|-------------------|
  | Waterfall | Low         | Poor          | Stable requirements |
  | Spiral    | High        | Excellent     | Complex, risky projects |

* **Exam Hotspots:**
  - **Feasibility Analysis:** Technical (can we build it?), Economic (Cost-Benefit: ROI = (Benefits - Costs)/Costs)
  - **COCOMO Types:** Organic (small teams), Semi-detached (medium), Embedded (complex)

* **Resource Kit:**
  - 🎥: "COCOMO Model Explained" (Gate Smashers, 8 min)
  - 📄: Javatpoint SDLC Cheat Sheet
  - 🧮: Online COCOMO Calculator

---

#### **Module-II: System Design [9L]**
* **Core Mechanics:**
  - **Context Diagram:** System as single bubble with external entities (e.g., ATM system interacting with Bank/Customer).
  - **DFD Levels:** Level 0 (overview) → Level 1 (key processes) → Level 2 (sub-processes).
  - **Top-Down Design:** Start with big picture → decompose (like organizing a book: Chapters → Sections → Paragraphs).
  - **Bottom-Up Design:** Combine small components into systems (like building LEGO sets).

* **Decision Tools:**
  - **Decision Tree:** Flowchart for actions (e.g., "If user > 65, apply senior discount").
  - **Decision Table:** Conditions vs. actions matrix (4 rules cover all combinations).

* **Key Comparisons:**
  | Approach      | Focus          | Flexibility | Example        |
  |---------------|----------------|-------------|----------------|
  | Functional    | Processes      | Low         | Banking systems |
  | Object-Oriented| Objects/Data   | High        | Game development |

* **Resource Kit:**
  - 🎥: "DFD vs Flowchart" (Neso Academy, 7 min)
  - 📄: TutorialsPoint Decision Table Guide
  - 🛠️: Draw.io for DFDs

---

#### **Module-III: Coding & Documentation [6L]**
* **Core Mechanics:**
  - **Structured Programming:** Linear code (functions, loops) like assembly instructions.
  - **OOP Principles:** Encapsulation (data + methods), Inheritance (parent-child classes), Polymorphism (same method, different behaviors).
  - **Information Hiding:** Expose only interfaces (e.g., car dashboard hides engine details).

* **Documentation:**
  - **System Docs:** User manuals (how to use), Tech specs (how it works).

* **Exam Hotspot:** Reuse = Leveraging libraries/templates to reduce coding (e.g., Java Collections).

* **Resource Kit:**
  - 🎥: "OOP in 9 Minutes" (Fireship, 9 min)
  - 📄: GeeksforGeeks OOP Cheat Sheet

---

#### **Module-IV: Testing [8L]**
* **Testing Levels:**
  ```
  Unit → Integration → System → Acceptance
  ```
* **Integration Strategies:**
  - **Big Bang:** Combine all modules at once (high risk).
  - **Incremental:** Top-down (stubs) or Bottom-up (drivers).

* **Test Case Template:**
  ```markdown
  Test ID | Input | Expected Output | Actual Output | Status
  T001    | x=5   | 25              | 25            | Pass
  ```

* **V&V:**
  - **Verification:** "Did we build it right?" (reviews).
  - **Validation:** "Did we build the right thing?" (user testing).

* **Resource Kit:**
  - 🎥: "Integration Testing Strategies" (Software Testing Mentor, 10 min)
  - 📄: Test Case Template (Guru99)

---

#### **Module-V: Project Management [8L]**
* **Core Mechanics:**
  - **Gantt Chart:** Visual timeline for scheduling (bars = task durations).
  - **SCM Checklist:** Version control (Git), Change requests, Baseline management.
  - **QA vs QC:** QA = *prevent* defects (process audits), QC = *detect* defects (testing).

* **Staffing Models:**
  - **Egoless:** Team ownership (no single "owner").
  - **Chief Programmer:** Lead directs work.

* **Exam Hotspot:** Earned Value Metrics:
  - `CPI = EV/AC` (CPI < 1 = over budget)

* **Resource Kit:**
  - 🎥: "Gantt Charts Explained" (Project Management, 6 min)
  - 📄: SCM Checklist (TutorialsPoint)

---

#### **Module-VI: Modelling Techniques [8L]**
* **Core Mechanics:**
  - **Static Models:** Structure (e.g., **Class Diagram**: `Customer ──◇ Order` for relationships).
  - **Dynamic Models:** Behavior (e.g., **Sequence Diagram**: Lifelines + arrows for interactions).

* **UML Quick Guide:**
  | Diagram        | Purpose                          | Key Symbols         |
  |----------------|----------------------------------|---------------------|
  | Class          | System structure                 | Boxes, arrows       |
  | Sequence       | Message flow over time           | Lifelines, → arrows |
  | State Chart    | Object state transitions         | Circles, arrows     |
  | Activity       | Workflow (like flowcharts)       | Diamonds (decisions)|

* **Key Comparison:**
  | Model Type   | Focus          | Example          |
  |--------------|----------------|------------------|
  | Static       | Structure      | Class Diagram    |
  | Dynamic      | Behavior       | Sequence Diagram |

* **Exam Hotspot:** Match diagram to need:
  - "Show login steps?" → **Sequence Diagram**
  - "Map user roles?" → **Class Diagram**

* **Resource Kit:**
  - 🎥: "UML in 10 mins" (Amigoscode, 10 min)
  - 🛠️: Lucidchart Free UML Tool
  - 📄: Visual Paradigm UML Cheat Sheet

---

### **Exam Power Tips**
1. **SDLC Models:** Memorize Waterfall/Spiral diagrams; COCOMO formula constants (a=2.4-3.0, b=1.05-1.20).
2. **Design:** Practice drawing Level 0 DFD for a restaurant system.
3. **Testing:** Know integration strategies for scenario questions.
4. **UML:** Identify diagrams from snippets (e.g., boxes + inheritance arrows = Class Diagram).
5. **PM:** Calculate CPI/SPI from given EV, AC, PV values.

**Final Resource Pack:**  
▶️ [Software Engineering Crash Course](https://youtu.be/O753uuutqH8) (15 min)  
📚 [All-in-One Cheat Sheet](https://www.tutorialspoint.com/software_engineering/software_engineering_quick_guide.htm)
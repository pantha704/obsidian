Below is a detailed, beginner-friendly explanation of Linear Programming (LPP) concepts, methods, and formulas. This explanation will tie together what you know from lines and planes (graphing, half-planes, intersections) with the process of optimizing a linear model. Read through each section carefully and try working out simple examples to build your confidence!

---

## 1. What Is Linear Programming?

**Linear Programming (LPP)** is an optimization technique used to determine the best outcome—such as maximum profit or minimum cost—subject to a set of linear constraints (relationships). In many real-world problems, you have limited resources (like time, money, or materials), and LPP helps you decide how to allocate those resources most effectively.

---

## 2. Key Components of an LPP

An LPP model is built using the following components:

- **Decision Variables:**  
  These variables represent the quantities you want to determine. For example, in a production problem, they might represent the number of units of different products. We usually denote these by \(x\), \(y\), or sometimes \(x_1\), \(x_2\).

- **Objective Function:**  
  This is a linear function that you need to maximize or minimize. For example, if you want to maximize profit, you might have:
  \[
  z = ax + by,
  \]
  where \(a\) and \(b\) are the profit contributions from each unit of \(x\) and \(y\).

- **Constraints:**  
  These are linear equations or inequalities representing restrictions such as limitations on resources (e.g., time, raw materials, labor). An example might be:
  \[
  3x + 4y \leq 100,
  \]
  which shows that a combination of \(x\) and \(y\) must not exceed a certain resource limit.

- **Non-Negativity Constraints:**  
  In many real-world situations, the decision variables cannot be negative. Thus, we include:
  \[
  x \geq 0, \quad y \geq 0.
  \]

---

## 3. Formulating an LPP

To build an LPP model from a problem statement, follow these steps:

1. **Identify Decision Variables:**  
   Decide which quantities to determine (e.g., units of products, amounts of resources used). Introduce variables such as \(x\) and \(y\) and include the condition:
   \[
   x,\, y \geq 0.
   \]

2. **Define the Objective Function:**  
   Write a linear function that describes what you want to optimize (maximize profit or minimize cost). For example:
   \[
   \text{Maximize } z = ax + by.
   \]

3. **Identify Constraints:**  
   Express the limitations or requirements as linear inequalities or equations. For example:
   \[
   \begin{aligned}
   a_1x + b_1y &\leq c_1, \\
   a_2x + b_2y &\leq c_2, \\
   \quad &\vdots \\
   x,\, y &\geq 0.
   \end{aligned}
   \]

*Tip:* Read the problem carefully so you capture every condition (like resource limits or production requirements).

---

## 4. Graphical Method for Solving LPPs

When you have only two decision variables, graphing the constraints can be very helpful. Here’s how you do it step by step:

### a. Graphing the Constraints

- **Convert the Inequalities:**  
  For each inequality (for example, \(ax + by \leq c\)), first graph the line:
  \[
  ax + by = c.
  \]
  This line represents the boundary of the inequality.

- **Determine the Half-Plane:**  
  Choose a test point (usually \((0,0)\) if it isn’t on the line) and substitute it into the inequality. If the inequality holds, shade the region that includes \((0,0)\); otherwise, shade the opposite half-plane.

### b. Identifying the Feasible Region

- **Feasible Region:**  
  This is the intersection of all the half-planes you have shaded. In essence, it is the set of all points \((x,y)\) that satisfy every constraint, including non-negativity (\(x, y \geq 0\)).

- **Convexity:**  
  A key property of the feasible region is that it is a convex set. This means that if you draw a line between any two points in the region, the entire line lies within the region. Convexity is important because it guarantees that any optimal solution will be on the boundary.

### c. Corner Point (Vertex) Method

- **Vertices and the Optimal Solution:**  
  The optimum value of the objective function (if a finite solution exists) is always found at one or more vertices (corner points) of the feasible region. This is known as the **convex polygon theorem**.

- **Steps Using the Vertex Method:**  
  1. **Graph the Constraints:** Find the feasible region by graphing and shading the appropriate half-planes.
  2. **Identify Vertices:** Determine the intersection points (vertices) of the boundary lines. This can be done by solving the simultaneous equations of the lines.
  3. **Evaluate the Objective Function:** Calculate the value of the objective function at each vertex.
  4. **Select the Optimal Value:** The maximum or minimum value among these is the solution to your problem.

- **Multiple Optimal Solutions:**  
  If two vertices yield the same optimum, then every point on the straight line connecting these vertices also gives that optimum.

- **Unbounded Feasible Regions:**  
  In cases where the feasible region is unbounded (extends indefinitely), the objective function might not have a finite maximum or minimum. In such problems, you must check whether the isoprofit or isocost lines can move indefinitely away from the origin while still staying within the feasible region.

---

## 5. Important Theorems

- **Theorem 1: Convexity of Feasible Solutions**  
  The set of all solutions that satisfy the constraints of an LPP forms a convex set. This property ensures that the line segment between any two feasible solutions will lie entirely within the feasible region.

- **Theorem 2: Convex Polygon (Corner Point) Theorem**  
  If an optimum (maximum or minimum) exists, it is found at one or more of the vertices (corner points) of the convex feasible region.

---

## 6. Examples of LPP Problems

Linear programming can model a variety of real-world problems. Here are a few common examples:

- **Resource Allocation:**  
  Determine the best way to use resources like raw materials, machine time, or labor to maximize profit or minimize cost. For instance, a company might use LPP to decide the optimal production mix of different products.

- **Production Planning:**  
  Find the optimal production levels for different products to meet demand while optimizing profits. Scenarios like manufacturing bicycles and tricycles can be modeled using LPP.

- **Diet Problems:**  
  Decide on the mix of foods or fodder that provides required nutrients at the lowest cost.

- **Transportation Problems:**  
  Optimize the transportation of goods from supply points to demand points to reduce total transportation costs.

---

## 7. Exercises and Applications

To gain a deep understanding and practical competence in LPP, practice is essential. Try the following types of exercises:

- **Finding Feasible Regions:**  
  Work on graphing inequalities and determining the overlapping (intersecting) region that satisfies all constraints.

- **Formulating LPPs:**  
  Convert word problems into mathematical models that include decision variables, objective functions, and constraints.

- **Solving LPPs Graphically:**  
  Use the corner point method to solve problems. Identify all vertices in the feasible region, substitute them into the objective function, and determine the optimum solution.

---

## Final Tips for Your Exams

- **Understand the Vocabulary:**  
  Make sure you’re comfortable with terms such as decision variables, objective function, constraints, feasible region, and vertex.

- **Step-by-Step Approach:**  
  Always start by writing down your decision variables, then the objective function, and finally the constraints. For problems involving two variables, draw a clear graph.

- **Practice Graphical Solutions:**  
  Being able to sketch out the feasible region and pinpoint the vertices is crucial for solving LPPs graphically.

- **Review Theorems:**  
  Knowing that the feasible region is convex and that an optimal solution (if it exists) occurs at a vertex will help you approach and verify your solutions.

By understanding these concepts and practicing various problems, you’ll develop the skills needed to tackle Linear Programming questions confidently on your exams. Good luck, and keep practicing!




---



Below are several steps and tips to ensure that the formulas display correctly in your Obsidian markdown reader:

---

### 1. Check That You're in Preview Mode

- **Edit Mode vs. Preview Mode:**  
  Obsidian only renders the LaTeX formulas (via its MathJax renderer) in Preview Mode. Make sure you switch from Edit Mode to Preview Mode to see the rendered equations.

---

### 2. Verify Delimiters for Math Formulas

- **Inline Math:**  
  Use single dollar signs for inline formulas. For example:  
  ```markdown
  $z = ax + by$
  ```
  
- **Display Math:**  
  Wrap block formulas in double dollar signs. For example:  
  ```markdown
	  $$
  3x + 4y \leq 100
  $$
  ```

- **Tip:**  
  Ensure there are no extra spaces before or after your dollar signs.

---

### 3. Check Your Obsidian Settings

- **Enable Math Rendering:**  
  Go to **Settings** → **Editor** (or **Markdown** settings, depending on your Obsidian version) and look for an option related to Math or LaTeX rendering (sometimes labelled "Enable Markdown Math" or similar).  
- **Update Obsidian:**  
  If you’re using an older version of Obsidian, consider updating to benefit from the latest improvements in the math rendering support.

---

### 4. Test with a Simple Note

Create a new note and add a simple formula to verify that the issue isn’t with your entire setup. For example, try copying and pasting this snippet:

```markdown
Here is an inline formula: $x^2 + y^2 = z^2$.

And here is a block formula:

$$
\frac{x- x_1}{a} = \frac{y- y_1}{b} = \frac{z- z_1}{c}
$$
```

Switch to Preview Mode to see if these formulas render correctly.

---

### 5. Consider Theme or Plugin Issues

- **Theme Compatibility:**  
  Sometimes a custom theme might interfere with math rendering. To test, switch to the default Obsidian theme.
- **Disable Conflicting Plugins:**  
  If you have community plugins installed, try disabling them one-by-one to see if one of them is causing the issue.

---

### 6. Alternative: Use Plain Text for Math (if needed)

If, for some reason, you cannot get the formulas to render, consider rewriting the formulas using plain text or using an image of the formula as a temporary measure until the math rendering issue is resolved.

---

By following these steps, you should be able to see the formulas rendered correctly in your Obsidian markdown reader. If you still encounter issues, checking the [Obsidian Forum](https://forum.obsidian.md/) or [Obsidian Help Docs](https://help.obsidian.md/) for any recent updates or known issues with math rendering may also provide additional guidance.

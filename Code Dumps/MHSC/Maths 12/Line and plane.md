
Below is a beginner‐friendly explanation of lines and planes in three-dimensional space. We’ll start with how to describe lines in 3D and then move on to planes. Try to read through each section slowly and work out a few examples by hand to build your confidence.

---

# Lines in 3D Space

A line in three dimensions is similar in idea to lines you know from 2D, but now points have three coordinates. There are several ways to describe a line.

## 1. Defining a Line

A line in 3D can be uniquely determined by either:

- **A Point and a Direction:** If you know one fixed point through which the line passes and the direction (given by a vector), you can describe the line completely.  
- **Two Distinct Points:** Knowing two different points tells you how to “draw” the line between them. The difference between their position vectors gives you the direction vectors.

---

## 2. Vector Equation of a Line

### a. Based on a Point and a Direction

Suppose you have a point A whose position vector is **a** and a direction vector **b**. Then any point **r** on the line can be written as:

\[
\mathbf{r} = \mathbf{a} + \lambda \mathbf{b}
\]

- **Explanation:**  
  The vector **a** sets the starting point and the term \(\lambda \mathbf{b}\) (where \(\lambda\) is a scalar that can vary over all real numbers) “moves” you along the direction of **b**. Positive values of \(\lambda\) move you one way, and negative values move you in the opposite direction.

### b. Based on Two Points

Suppose you are given two points A and B with position vectors **a** and **b**, respectively. Then the direction of the line is given by \(\mathbf{b} - \mathbf{a}\), and the equation becomes:

\[
\mathbf{r} = \mathbf{a} + \lambda (\mathbf{b} - \mathbf{a})
\]

- **Tip:**  
  Here, when \(\lambda = 0\) you are at point A and when \(\lambda = 1\) you are at point B.

---

## 3. Cartesian Equations of a Line

Often you may see the equation of a line written in a form that relates the x, y, and z coordinates.

### a. Parametric Form

If the given point is \(A(x_1, y_1, z_1)\) and the direction ratios (components of the direction vector) are \(a\), \(b\), and \(c\), then the parametric equations are:

\[
\begin{aligned}
x &= x_1 + \lambda a, \\
y &= y_1 + \lambda b, \\
z &= z_1 + \lambda c.
\end{aligned}
\]

### b. Symmetric (or Cartesian) Form

Assuming none of the direction ratios is zero (so you can divide by them), the equations can be written as:

\[
\frac{x - x_1}{a} = \frac{y - y_1}{b} = \frac{z - z_1}{c}.
\]

- **When Not to Use:** If one (or more) of the ratios \(a\), \(b\), or \(c\) equals zero, then the parametric form is preferred.

*Note:* When you see direction cosines (denoted by \(l\), \(m\), and \(n\)) instead of direction ratios, the parametric form looks similar:
\[
x = x_1 + \lambda l,\quad y = y_1 + \lambda m,\quad z = z_1 + \lambda n.
\]
Here, \(\lambda\) also represents the distance along the line (with sign indicating direction).

---

## 4. Direction Ratios and Direction Cosines

- **Direction Ratios:**  
  If the direction vector of a line is given as
  \[
  \mathbf{b} = a\,\hat{i} + b\,\hat{j} + c\,\hat{k},
  \]
  then \(a\), \(b\), and \(c\) are the direction ratios.

- **Direction Cosines:**  
  These are the cosines of the angles that the line makes with the coordinate axes. They are obtained by dividing the direction ratios by the vector’s magnitude:
  \[
  l = \frac{a}{\sqrt{a^2+b^2+c^2}},\quad m = \frac{b}{\sqrt{a^2+b^2+c^2}},\quad n = \frac{c}{\sqrt{a^2+b^2+c^2}}.
  \]
  They satisfy:
  \[
  l^2 + m^2 + n^2 = 1.
  \]

---

## 5. Distance of a Point from a Line

To find the distance from a point \(P\) (with position vector \(\boldsymbol{\alpha}\)) to a line given by

\[
\mathbf{r}=\mathbf{a}+\lambda\mathbf{b},
\]

use the formula:

\[
d = \frac{\left\vert (\boldsymbol{\alpha} - \mathbf{a}) \times \mathbf{b} \right\vert}{\left\vert \mathbf{b} \right\vert}.
\]

- **How It Works:**  
  The cross product \((\boldsymbol{\alpha} - \mathbf{a}) \times \mathbf{b}\) gives a vector whose magnitude is proportional to the area of the parallelogram formed by \(\boldsymbol{\alpha} - \mathbf{a}\) and \(\mathbf{b}\). Dividing by \(|\mathbf{b}|\) “extracts” the height (i.e., the perpendicular distance).

---

## 6. Angle Between Two Lines

The angle between two lines is the angle between their direction vectors. Suppose the two lines have direction vectors \(\mathbf{b}_1\) and \(\mathbf{b}_2\); then:

\[
\cos \theta = \frac{\mathbf{b}_1 \cdot \mathbf{b}_2}{\left\vert \mathbf{b}_1 \right\vert \left\vert \mathbf{b}_2 \right\vert}.
\]

- **Tip:**  
  Use the dot product to find the cosine of the angle. If the cosine is close to 1, the lines are almost parallel, and if it is close to 0, the lines are nearly perpendicular.

---

## 7. Coplanarity of Two Lines

Two lines are coplanar (i.e., lie in the same plane) if the vector connecting points on them is “compatible” with the directions of the lines.

- **Vector Test:**  
  For lines given by
  \[
  \mathbf{r} = \mathbf{a}_1 + \lambda \mathbf{b}_1 \quad \text{and} \quad \mathbf{r}=\mathbf{a}_2 + \mu \mathbf{b}_2,
  \]
  they are coplanar if
  \[
  (\mathbf{a}_2 - \mathbf{a}_1) \cdot (\mathbf{b}_1 \times \mathbf{b}_2) = 0.
  \]
  If the determinant
  \[
  \begin{vmatrix}
  x_2 - x_1 & y_2 - y_1 & z_2 - z_1 \\
  a_1       & b_1       & c_1       \\
  a_2       & b_2       & c_2       
  \end{vmatrix} = 0,
  \]
  the lines are coplanar.

- **Note:**  
  If two lines are nonparallel and coplanar, they will intersect or be parallel. The “shortest distance” between them is zero if they intersect.

---

## 8. Shortest Distance Between Skew Lines

Skew lines are nonparallel lines that do not lie in the same plane. The shortest (perpendicular) distance between two skew lines given by

\[
\mathbf{r}=\mathbf{a}_1+\lambda \mathbf{b}_1 \quad \text{and} \quad \mathbf{r}=\mathbf{a}_2+\mu \mathbf{b}_2
\]

is:

\[
d = \frac{\left\vert (\mathbf{a}_2-\mathbf{a}_1)\cdot (\mathbf{b}_1 \times \mathbf{b}_2) \right\vert}{\left\vert \mathbf{b}_1 \times \mathbf{b}_2 \right\vert}.
\]

- **How It Works:**  
  The numerator computes the volume of a parallelepiped (which also involves the separation of the lines) and dividing by the area of the base (given by \(|\mathbf{b}_1 \times \mathbf{b}_2|\)) gives the height—the shortest distance.

---

## 9. Distance Between Parallel Lines

For two parallel lines (same direction vector) given by

\[
\mathbf{r}=\mathbf{a}_1+\lambda \mathbf{b} \quad \text{and} \quad \mathbf{r}=\mathbf{a}_2+\lambda \mathbf{b},
\]

the shortest distance is given by:

\[
d = \frac{\left\vert (\mathbf{a}_2-\mathbf{a}_1) \times \mathbf{b} \right\vert}{\left\vert \mathbf{b} \right\vert}.
\]

- **Why It Works:**  
  The cross product \((\mathbf{a}_2 - \mathbf{a}_1) \times \mathbf{b}\) gives the area of a parallelogram with base \(|\mathbf{b}|\) and height equal to the distance between the lines.

---

# Planes in 3D Space

A plane is a flat, two-dimensional surface that extends infinitely in every direction. There are many ways to define a plane.

## 1. Defining a Plane

A plane can be described by:

- **Three Non-collinear Points:** Points that do not lie on a single line determine a unique plane.
- **A Point and a Line:** A point not on the line and the line itself determine the plane.
- **A Point and Two Nonparallel Vectors:** The plane is “spanned” by the two directions.
- **A Point and a Normal:** A line perpendicular (normal) to the plane gives a very convenient definition.

A line perpendicular to a plane is called a **normal** to the plane.

---

## 2. Vector Equation of a Plane

### a. Using a Point and a Normal Vector

Let a plane pass through a point A with position vector **a** and have a normal vector **n**. Then every point **r** in the plane satisfies:

\[
(\mathbf{r} - \mathbf{a})\cdot\mathbf{n} = 0.
\]

- **Alternate Form:**  
  If we let \(d = \mathbf{a}\cdot\mathbf{n}\), then the equation can be written as:
  \[
  \mathbf{r}\cdot\mathbf{n} = d.
  \]

### b. Using a Point and Two Parallel Vectors (Parametric Form)

If a plane passes through the point A (with vector **a**) and is parallel to two nonparallel vectors **b** and **c**, every point **r** in the plane can be written as:

\[
\mathbf{r} = \mathbf{a} + \lambda \mathbf{b} + \mu \mathbf{c},
\]

where \(\lambda\) and \(\mu\) are real numbers. This is the **parametric form** of the plane.

### c. Through Three Non-collinear Points

If the plane passes through points A, B, and C (with position vectors **a**, **b**, and **c**), its vector equation is:

\[
(\mathbf{r} - \mathbf{a})\cdot \left[ (\mathbf{b} - \mathbf{a}) \times (\mathbf{c} - \mathbf{a}) \right] = 0.
\]

- **Explanation:**  
  The cross product \((\mathbf{b} - \mathbf{a}) \times (\mathbf{c} - \mathbf{a})\) gives a normal vector to the plane.

---

## 3. Cartesian Equation of a Plane

### a. Through a Point with a Given Normal

If a plane passes through the point \(A(x_1, y_1, z_1)\) and has a normal with direction ratios \(a\), \(b\), and \(c\), its Cartesian (or scalar) equation is:

\[
a(x - x_1) + b(y - y_1) + c(z - z_1) = 0.
\]

### b. Through Three Non-collinear Points (Using a Determinant)

For points \(A(x_1,y_1,z_1)\), \(B(x_2,y_2,z_2)\), and \(C(x_3,y_3,z_3)\), the plane’s equation can be written as the determinant:

```markdown
| x - x₁   y - y₁   z - z₁ |
| x₂ - x₁  y₂ - y₁  z₂ - z₁ | = 0
| x₃ - x₁  y₃ - y₁  z₃ - z₁ |
```

- **Idea:**  
  A zero determinant indicates that the three vectors are coplanar.

### c. Normal Form

In the normal form, if the unit normal vector is \(\hat{n} = (l, m, n)\) and the distance from the origin to the plane is \(p\), the equation is:

\[
lx + my + nz = p.
\]

---

## 4. Intercepts

If a plane intercepts the coordinate axes at \(a\) (x-intercept), \(b\) (y-intercept), and \(c\) (z-intercept) (none being zero), one can write the equation in intercept form as:

\[
\frac{x}{a} + \frac{y}{b} + \frac{z}{c} = 1.
\]

- **Alternate Vector Form:**  
  Sometimes you might see the equation written in a form that involves the product \(abc\) and the intercepts as coefficients for the unit vectors.

---

## 5. Plane Through the Intersection of Two Planes

Suppose you have two planes:
\[
\mathbf{r}\cdot\mathbf{n}_1 = d_1 \quad \text{and} \quad \mathbf{r}\cdot\mathbf{n}_2 = d_2.
\]
A family of planes passing through their line of intersection is given by a linear combination of the two equations:

\[
\mathbf{r}\cdot(\mathbf{n}_1 + \lambda\,\mathbf{n}_2) = d_1 + \lambda\,d_2,
\]

where \(\lambda\) is a parameter.

In Cartesian form, if the given planes are

\[
a_1x+b_1y+c_1z+d_1 = 0 \quad \text{and} \quad a_2x+b_2y+c_2z+d_2 = 0,
\]

the combined plane’s equation is:

\[
(a_1x+b_1y+c_1z+d_1) + \lambda(a_2x+b_2y+c_2z+d_2) = 0.
\]

---

## 6. Angle Between Two Planes

The angle between two planes is defined as the angle between their normal vectors. If the normals are \(\mathbf{n}_1\) and \(\mathbf{n}_2\), then:

\[
\cos \theta = \frac{\mathbf{n}_1 \cdot \mathbf{n}_2}{\left\vert \mathbf{n}_1 \right\vert \left\vert \mathbf{n}_2 \right\vert}.
\]

- **Tip:**  
  If the normals are nearly parallel, the planes make a small angle, and vice versa.

---

## 7. Angle Between a Line and a Plane

The angle between a line and a plane is defined as the complement of the angle between the line’s direction vector \(\mathbf{b}\) and the plane’s normal \(\mathbf{n}\). In other words, if \(\theta\) is the angle between the line and the plane, then:

\[
\sin \theta = \frac{\left\vert \mathbf{b} \cdot \mathbf{n} \right\vert}{\left\vert \mathbf{b} \right\vert \left\vert \mathbf{n} \right\vert}.
\]

- **Why Sine?**  
  Because the smaller the angle between the line and the plane’s normal, the closer the line is to being parallel to the plane. Taking the complement gives the actual angle between the line and the plane.

---

## 8. Distance of a Point from a Plane

If you have a plane in the normal form:

\[
\mathbf{r}\cdot\hat{n} = p,
\]

where \(\hat{n}\) is a unit normal vector and \(p\) is the perpendicular distance from the origin, then:

- **Distance from the Origin:**  
  It is simply \(p\).
  
- **Distance from Any Point A (with position vector \(\mathbf{a}\)):**

\[
\text{Distance} = \left\vert \mathbf{a}\cdot\hat{n} - p \right\vert.
\]

- **Explanation:**  
  This formula gives the shortest (perpendicular) distance from the point to the plane.

---

# Final Tips

- **Take It One Step at a Time:**  
  Start with understanding the vector form of lines and planes. Then, move on to writing their Cartesian equations.
  
- **Practice Drawing Diagrams:**  
  Sketching a line or a plane with a given point and direction (or normal) can significantly help your visualization.

- **Work Through Examples:**  
  The formulas may seem daunting at first, but practice with numerical examples will help you see how they are used. For instance, try finding the line connecting two given points or the distance from a point to a plane.

- **Connect With Earlier Topics:**  
  Concepts like the dot product and cross product (from your vector studies) are essential for finding angles and distances. Make sure you are comfortable with these operations.

With consistent study and practice, these ideas will gradually become clear. Good luck with your exams, and remember: breaking problems down into smaller pieces often makes them much easier to manage!

Happy Studying!

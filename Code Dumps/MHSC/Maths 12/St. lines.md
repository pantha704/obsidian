
Below is a detailed, beginner-friendly explanation of pairs of straight lines. Read through each section slowly and try to work out simple examples by hand. This should help you build a strong foundation for your exams.

---

## 1. Combined Equation of a Pair of Lines

When we want one equation to represent two lines at the same time, we use a **combined equation**.

- **Idea:**  
  If you have two lines whose equations are  
  \[
  u \equiv a_1x + b_1y + c_1 = 0 \quad \text{and} \quad v \equiv a_2x + b_2y + c_2 = 0,
  \]  
  then multiplying these equations gives  
  \[
  u \times v = 0.
  \]
- **What It Means:**  
  The product \( uv = 0 \) is zero if either \( u = 0 \) or \( v = 0 \). Thus, it represents the two lines simultaneously.
- **Separate Equations:**  
  The equations \( u = 0 \) and \( v = 0 \) are called the **separate equations** of the two lines.

---

## 2. Homogeneous Equation of Degree Two

A **homogeneous equation of degree two** is written in the form:  
\[
ax^2 + 2hxy + by^2 = 0.
\]

- **Properties:**
  - Every term is of degree 2 (for instance, \( x^2 \), \( xy \), and \( y^2 \)).
  - Because every term has the same degree, the graph of this equation (if it represents lines) must pass through the origin \((0, 0)\).

- **Discriminant Condition:**
  - The key expression here is **\( h^2 - ab \)**.
    - If \( h^2 - ab > 0 \): Two distinct real lines.
    - If \( h^2 - ab = 0 \): The two lines coincide (they are the same line repeated).
    - If \( h^2 - ab < 0 \): No real lines are represented.

---

## 3. Slopes of the Lines

To find the slopes of the lines represented by  
\[
ax^2 + 2hxy + by^2 = 0,
\]  
we substitute \( y = m x \) (where \( m \) is the slope).

- **Step-by-Step:**
  1. Substitute \( y = mx \) into the equation:
     \[
     ax^2 + 2hmx^2 + bm^2x^2 = 0.
     \]
  2. Factor out \( x^2 \) (assuming \( x \neq 0 \)):
     \[
     a + 2hm + bm^2 = 0.
     \]
  3. Write the quadratic in \( m \) as:
     \[
     bm^2 + 2hm + a = 0.
     \]

- **Results:**
  - **Sum of the slopes:** \( m_1 + m_2 = -\dfrac{2h}{b} \).
  - **Product of the slopes:** \( m_1 m_2 = \dfrac{a}{b} \).

*This quadratic is sometimes called the auxiliary equation.*

---

## 4. Angle Between the Lines

The acute angle \( \theta \) between the two lines (when represented by \( ax^2+2hxy+by^2=0 \)) can be found using:
\[
\tan \theta = \left|\dfrac{2\sqrt{h^2 - ab}}{a+b}\right|.
\]

- **Special Note:**  
  If \( a + b = 0 \), then the tangent becomes undefined (or infinite), which implies the lines are perpendicular.

---

## 5. General Second-Degree Equation

The **general second-degree equation** in \( x \) and \( y \) is:
\[
ax^2 + 2hxy + by^2 + 2gx + 2fy + c = 0.
\]

- **Representing a Pair of Lines:**  
  Such an equation can represent a pair of straight lines (not necessarily through the origin) if it can be factored into two linear factors.
  
- **Conditions for Representing a Pair of Lines:**
  1. **Determinant Condition:**  
     \[
     abc + 2fgh - af^2 - bg^2 - ch^2 = 0.
     \]
  2. **Discriminant Condition:**  
     \( h^2 - ab \geq 0 \).

---

## 6. Parallel and Perpendicular Lines

For lines represented by the homogeneous equation \( ax^2+2hxy+by^2=0 \):

- **Parallel (Coincident) Lines:**  
  If \( h^2 - ab = 0 \), then the lines are coincident; that is, they share the same slope and lie on top of each other.
  
- **Perpendicular Lines:**  
  The lines are perpendicular if  
  \[
  a + b = 0.
  \]
  (This condition ensures the product of the slopes \( m_1m_2 = -1 \).)

---

## 7. Bisectors of the Angles

The **angle bisectors** are the lines that exactly split the angles between the two given lines. For the pair represented by:
\[
ax^2 + 2hxy + by^2 = 0,
\]
the combined equation for the bisectors is:
\[
hx^2 - (a-b)xy - hy^2 = 0.
\]

- **Key Point:**  
  The two bisectors of the angles between the lines are always perpendicular to each other.

---

## 8. Key Points to Remember

- **Not Every Homogeneous Quadratic Represents Two Lines:**  
  The equation \( ax^2+2hxy+by^2=0 \) represents a pair of lines only if \( h^2-ab \geq 0 \).

- **Special Case \( b = 0 \):**  
  If \( b = 0 \), one of the lines is the Y-axis.

- **Auxiliary Equation:**  
  The quadratic in \( m \), given by  
  \[
  bm^2 + 2hm + a = 0,
  \]
  has roots that are the slopes of the lines.

---

## 9. Using Special Conditions (Practice Problems)

Often, exam problems provide extra conditions that lead to specific relationships between the coefficients \( a \), \( h \), and \( b \). Here are a few examples:

1. **Perpendicularity to a Given Line:**  
   If one of the lines from \( ax^2+2hxy+by^2=0 \) is perpendicular to \( px+qy=0 \), then:
   \[
   ap^2 + 2hpq + bq^2 = 0.
   \]

2. **One Slope Four Times the Other:**  
   If one line’s slope is four times that of the other, the relationship is:
   \[
   16h^2 = 25ab.
   \]

3. **Angle Bisector as One of the Lines:**  
   If one of the lines bisects the angle between the coordinate axes, then:
   \[
   (a+b)^2 = 4h^2.
   \]

4. **One Slope is Three Times the Other:**  
   The condition becomes:
   \[
   3h^2 = 4ab.
   \]

5. **Coincidence with a Given Line:**  
   For instance, if the line \( 4x - 5y = 0 \) coincides with one of the lines, then:
   \[
   25a + 40h + 16b = 0.
   \]

6. **Equal Angles between Two Different Pairs of Lines:**  
   If the angle between the lines represented by \( ax^2+2hxy+by^2=0 \) is the same as the angle between the lines represented by \( 2x^2 - 5xy + 3y^2 = 0 \), then:
   \[
   100(h^2 - ab) = (a+b)^2.
   \]

7. **One Slope is the Square of the Other:**  
   Then the relationship is:
   \[
   a^2b + ab^2 + 8h^3 = 6abh.
   \]

8. **Equilateral Triangle Formation with a Given Line:**  
   If the lines form an equilateral triangle with \( lx + my = 1 \), then:
   \[
   (3a + b)(a + 3b) = 4h^2.
   \]

9. **Lines Perpendicular to the Given Pair:**  
   The combined equation of the pair of lines passing through the origin and perpendicular to the lines represented by \( ax^2+2hxy+by^2=0 \) is:
   \[
   bx^2 - 2hxy + ay^2 = 0.
   \]

*Remember:* These relationships come from applying conditions (like slopes, angles, or perpendicularity) to the general forms. When solving exam problems, start with the general form and then substitute the extra information to obtain these relationships.

---

## Final Tips for Your Exam

- **Understand the Concepts:**  
  Know the definitions (e.g., what a homogeneous equation is, how a combined equation works) rather than just memorizing formulas.

- **Practice with Examples:**  
  Work on sample problems where you factor a quadratic into two linear factors, calculate slopes, and use the angle formula.

- **Write Down All Key Conditions:**  
  Always check the discriminant \( h^2 - ab \) to determine whether real lines exist, and pay attention to special cases (like \( b=0 \) or \( a+b=0 \)).

- **Organize Your Work:**  
  When approaching a problem, clearly outline which part of the theory you are using (for instance, “the slopes are given by the roots of \( bm^2+2hm+a=0 \)”).

Good luck with your revision! If you have any further questions or need more examples on a specific point, feel free to ask. Happy studying!

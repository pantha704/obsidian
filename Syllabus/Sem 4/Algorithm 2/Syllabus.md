Here's a concise breakdown of each module:

### Module-I: Amortized Analysis
Based on the Cornell CS lecture notes, there are three main methods:
1. **Aggregate Method:** Analyzes total cost of sequence of operations divided by number of operations
2. **Accounting (Banker's) Method:** Assigns "credits" to operations, saving for expensive operations
3. **Potential Method:** Uses a potential function to track the state of data structure

Example: Binary Counter
- Traditional analysis shows O(log n) per increment
- Amortized analysis proves only O(1) per increment averaged over sequence

### Module-II: Linear Time Sorting
- **Counting Sort:** O(n+k) time where k is range of input
- **Radix Sort:** Sorts by processing each digit position
- **Bucket Sort:** Distributes elements into buckets, then sorts buckets

### Module-III: Approximation Algorithms
- **Vertex Cover:** Finding minimum set of vertices that touch all edges
- **Traveling Salesman:** Finding shortest route visiting all cities
- **Set Cover:** Selecting minimum number of sets to cover all elements
- Uses randomization and linear programming for approximations

### Module-IV: Computational Geometry
- **Line Segment Properties:** Intersections, orientation
- **Convex Hull:** Finding smallest convex polygon containing all points
- **Closest Pair:** Finding two closest points in a set

### Module-V: NP Completeness
- **Classes:**
  - P: Problems solvable in polynomial time
  - NP: Problems verifiable in polynomial time
  - NP-Complete: Hardest problems in NP
  - NP-Hard: At least as hard as NP-Complete problems
- **Cook's Theorem:** Proves SAT is NP-Complete

### Module-VI: Advanced Topics
- **DFT & FFT:** Fast Fourier Transform algorithms
- **Integer Multiplication:** Efficient algorithms for large numbers
- **Approximation Schemes:**
  - PTAS (Polynomial Time Approximation Scheme)
  - Performance guarantees
  - Trade-off between running time and solution quality

For exam preparation, focus on:
1. Understanding amortized analysis methods with examples
2. Linear sorting algorithms and their time complexities
3. Basic approximation algorithms and their ratios
4. NP-completeness concepts and problem classifications
5. Key geometric algorithms and their applications

[Source: Cornell CS 312 Lecture Notes](http://www.cs.cornell.edu/courses/cs312/2006sp/lectures/lec18.html)

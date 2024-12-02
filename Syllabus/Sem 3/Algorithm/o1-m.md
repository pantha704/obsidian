
# Comprehensive Study Guide for Your Exam

Here's a detailed explanation of all the topics across the four modules to help you prepare effectively for your exam.

---

## Module-I: Introduction

### 1. **Characterizing Features of an Algorithm**
Understanding what makes an algorithm effective is crucial. The key features include:

- **Correctness**: The algorithm should produce the expected output for all valid inputs.
- **Efficiency**: It should perform tasks using minimal resources (time and space).
- **Simplicity**: Clear and understandable logic makes the algorithm easier to implement and debug.
- **Determinism**: Given the same input, the algorithm should always produce the same output.
- **Scalability**: Ability to handle larger inputs without a significant loss in performance.

### 2. **Performance Analysis**
Evaluating how well an algorithm performs involves assessing:

- **Time Complexity**: Measures the amount of time an algorithm takes to complete as a function of the input size.
- **Space Complexity**: Measures the amount of memory an algorithm uses relative to the input size.

### 3. **Time and Space Complexities**

#### **Worst Case and Average Case**
- **Worst Case**: The maximum time or space an algorithm requires for any input of size *n*. It provides an upper bound.
- **Average Case**: The expected time or space over all possible inputs of size *n*. It gives a more realistic performance measure for typical inputs.

### 4. **Asymptotic Notations**
Asymptotic notations describe the behavior of algorithms as the input size grows towards infinity.

- **Big O (O)**: Represents the upper bound of an algorithm's running time. It describes the worst-case scenario.
  - *Example*: O(n log n) for Merge Sort.
  
- **Small o (o)**: Represents a loose upper bound that is not tight. It means the algorithm grows strictly slower than the given function.
  - *Example*: If an algorithm is o(n²), it grows slower than n².
  
- **Big Omega (Ω)**: Represents the lower bound of an algorithm's running time. It describes the best-case scenario.
  - *Example*: Ω(n) for linear search.
  
- **Small Omega (ω)**: Represents a loose lower bound that is not tight. It means the algorithm grows strictly faster than the given function.
  - *Example*: If an algorithm is ω(1), it grows faster than a constant.
  
- **Theta (Θ)**: Represents a tight bound where the algorithm's running time grows at the same rate both in the upper and lower bounds.
  - *Example*: Θ(n) for linear search in the best and average cases.

---

## Module-II: Foundations of Design and Analysis

## Understanding Algorithmic Paradigms

When you're new to algorithms, grasping the fundamental paradigms is essential. These paradigms are overarching strategies for solving a wide range of problems. Here's a brief overview of each, along with practical examples to illustrate their use cases.



## 1. Divide and Conquer

### **Concept**
Divide and Conquer breaks a problem into smaller, more manageable subproblems, solves each subproblem independently, and then combines their solutions to solve the original problem.

### **How It Works**
1. **Divide**: Split the problem into smaller subproblems.
2. **Conquer**: Solve each subproblem recursively.
3. **Combine**: Merge the solutions of the subproblems to form the solution to the original problem.

### **Example Use Case: Merge Sort**

**Problem**: Sorting an array of numbers.

**How Merge Sort Uses Divide and Conquer**:
1. **Divide** the array into two halves.
2. **Conquer** by recursively sorting each half.
3. **Combine** the two sorted halves to produce a sorted array.

```typescript
function mergeSort(arr: number[]): number[] {
  if (arr.length ≤ 1) return arr;

  const mid = Math.floor(arr.length / 2);
  const left = mergeSort(arr.slice(0, mid));
  const right = mergeSort(arr.slice(mid));

  return merge(left, right);
}

function merge(left: number[], right: number[]): number[] {
  let result: number[] = [];
  let i = 0, j = 0;

  while (i < left.length && j < right.length) {
    if (left[i] < right[j]) result.push(left[i++]);
    else result.push(right[j++]);
  }

  return result.concat(left.slice(i)).concat(right.slice(j));
}
```

---

## 2. Greedy

### **Concept**
Greedy algorithms make a sequence of choices, each of which looks the best at the moment. The hope is that by choosing locally optimal solutions, a global optimum will be reached.

### **How It Works**
1. **Choose** the best available option at each step.
2. **Repeat** until the problem is solved.
3. **No Backtracking**: Once a choice is made, it is never reconsidered.

### **Example Use Case: Prim’s Algorithm for Minimum Spanning Tree (MST)**

**Problem**: Connect all vertices in a graph with the minimal total edge weight without forming cycles.

**How Prim’s Uses Greedy**:
1. Start with any vertex.
2. At each step, add the smallest edge that connects a vertex in the tree to a vertex outside the tree.
3. Repeat until all vertices are included.

```typescript
function primMST(graph: number[][]): number {
  const V = graph.length;
  const selected = Array(V).fill(false);
  selected[0] = true; // Start from vertex 0
  let mstWeight = 0;

  for (let count = 0; count < V - 1; count++) {
    let min = Infinity;
    let x = 0, y = 0;

    for (let i = 0; i < V; i++) {
      if (selected[i]) {
        for (let j = 0; j < V; j++) {
          if (!selected[j] && graph[i][j] < min) {
            min = graph[i][j];
            x = i;
            y = j;
          }
        }
      }
    }

    mstWeight += min;
    selected[y] = true;
  }

  return mstWeight;
}
```

---

## 3. Dynamic Programming

### **Concept**
Dynamic Programming (DP) solves problems by breaking them down into overlapping subproblems, solving each subproblem once, and storing their solutions (usually in a table) to avoid redundant computations.

### **How It Works**
1. **Identify** the subproblems.
2. **Solve** each subproblem and **store** their results.
3. **Combine** the stored solutions to solve larger problems.

### **Example Use Case: Fibonacci Sequence**

**Problem**: Calculate the nth Fibonacci number.

**How DP Solves It**:
Instead of recalculating Fibonacci numbers repeatedly, store the results of previous calculations.

```typescript
function fibonacci(n: number): number {
  if (n ≤ 1) return n;
  const dp = Array(n + 1).fill(0);
  dp[1] = 1;

  for (let i = 2; i ≤ n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }

  return dp[n];
}
```

---

## 4. Backtracking

### **Concept**
Backtracking explores all possible solutions by incrementally building candidates and abandoning a candidate ("backtracking") as soon as it's determined that it cannot lead to a valid solution.

### **How It Works**
1. **Build** solutions incrementally.
2. **Check** if the current solution is valid.
3. **Backtrack** if the solution cannot be completed successfully, and try another path.

### **Example Use Case: Eight Queens Problem**

**Problem**: Place eight queens on an 8×8 chessboard so that no two queens threaten each other.

**How Backtracking Solves It**:
1. Place a queen in a column.
2. Move to the next column and place a queen in a valid row.
3. If no valid row is found, backtrack to the previous column and move the queen to the next valid row.
4. Repeat until all queens are placed.

```typescript
function solveNQueens(N: number): number[][] {
  const solutions: number[][] = [];
  const board: number[] = [];

  function isSafe(row: number, col: number): boolean {
    for (let i = 0; i < col; i++) {
      if (board[i] === row || Math.abs(board[i] - row) === col - i) return false;
    }
    return true;
  }

  function backtrack(col: number) {
    if (col === N) {
      solutions.push([...board]);
      return;
    }

    for (let row = 0; row < N; row++) {
      if (isSafe(row, col)) {
        board[col] = row;
        backtrack(col + 1);
      }
    }
  }

  backtrack(0);
  return solutions;
}
```

---

# Summary

- **Divide and Conquer**: Break problems into independent subproblems, solve them recursively, and combine solutions. *Example*: Merge Sort.
- **Greedy**: Make the best immediate choice at each step. *Example*: Prim’s Algorithm for MST.
- **Dynamic Programming**: Solve overlapping subproblems and store their solutions to avoid redundancy. *Example*: Fibonacci Sequence.
- **Backtracking**: Explore all possible solutions and backtrack when a path doesn't lead to a solution. *Example*: Eight Queens Problem.

Understanding these paradigms will equip you with versatile strategies to tackle a wide array of algorithmic challenges. Practice implementing each paradigm with various problems to solidify your comprehension and application skills.


---

## Module-III: Sorting Algorithms

# Simplified Guide to Sorting Algorithms

If you're new to algorithms, understanding sorting methods is a great starting point. Here's a brief overview of key sorting algorithms and their use cases to help you grasp the basics quickly.

---

## 1. Lower Bound on Time Complexity

### **What It Means**
- **O(n log n)** is the fastest possible time complexity for comparison-based sorting algorithms.
- **Implication**: No comparison-based sort can consistently sort faster in the worst case.

### **Why It’s Important**
- Helps you understand the efficiency limits of sorting methods.
- Guides you in choosing the right algorithm based on performance needs.

---

## 2. Quicksort

### **Type**
- **Divide and Conquer**

### **Time Complexity**
- **Average Case**: O(n log n)
- **Worst Case**: O(n²)

### **How It Works**
1. **Choose a Pivot**: Select an element to divide the array.
2. **Partition**: Rearrange elements so those less than the pivot come before it, and those greater come after.
3. **Recursively Sort**: Apply the same process to the sub-arrays on either side of the pivot.

### **Use Case**
- **Efficient General-Purpose Sort**: Suitable for large datasets due to its average-case efficiency.
  
```typescript
function quickSort(arr: number[]): number[] {
  if (arr.length <= 1) return arr;

  const pivot = arr[arr.length - 1];
  const left = arr.filter(x => x < pivot);
  const right = arr.filter(x => x !== pivot && x >= pivot);

  return [...quickSort(left), pivot, ...quickSort(right)];
}
```

---

## 3. Merge Sort

### **Type**
- **Divide and Conquer**

### **Time Complexity**
- **All Cases**: O(n log n)

### **How It Works**
1. **Divide**: Split the array into two halves.
2. **Conquer**: Recursively sort each half.
3. **Combine**: Merge the sorted halves to form a single sorted array.

### **Use Case**
- **Stable Sorting**: Ideal when maintaining the original order of equal elements is important.

```typescript
function mergeSort(arr: number[]): number[] {
  if (arr.length <= 1) return arr;

  const mid = Math.floor(arr.length / 2);
  const left = mergeSort(arr.slice(0, mid));
  const right = mergeSort(arr.slice(mid));

  return merge(left, right);
}

function merge(left: number[], right: number[]): number[] {
  let result: number[] = [];
  let i = 0, j = 0;

  while (i < left.length && j < right.length) {
    if (left[i] < right[j]) result.push(left[i++]);
    else result.push(right[j++]);
  }

  return result.concat(left.slice(i)).concat(right.slice(j));
}
```

---

## 4. Counting Sort

### **Type**
- **Non-Comparison Based**

### **Time Complexity**
- **O(n + k)** where *n* is the number of elements and *k* is the range of input.

### **How It Works**
1. **Count**: Tally the occurrences of each unique element.
2. **Calculate Positions**: Determine the position of each element in the sorted array based on counts.
3. **Place Elements**: Insert elements into the final sorted array using the calculated positions.

### **Use Case**
- **When Range (k) is Small**: Efficient for sorting integers within a known, limited range.

```typescript
function countingSort(arr: number[]): number[] {
  const max = Math.max(...arr);
  const count = Array(max + 1).fill(0);
  
  arr.forEach(num => count[num]++);
  
  let sorted: number[] = [];
  count.forEach((cnt, num) => {
    for (let i = 0; i < cnt; i++) sorted.push(num);
  });
  
  return sorted;
}
```

---

## 5. Radix Sort

### **Type**
- **Non-Comparison Based**

### **Time Complexity**
- **O(d * (n + k))** where *d* is the number of digits, *n* is the number of elements, and *k* is the range of digits.

### **How It Works**
1. **Sort by Least Significant Digit (LSD)**: Start sorting from the rightmost digit.
2. **Repeat for Each Digit**: Move leftward, sorting by each subsequent digit.
3. **Use a Stable Sort**: Ensure that the relative order of elements with the same digit is maintained.

### **Use Case**
- **Large Datasets with Fixed-Length Keys**: Efficient for sorting numbers or strings where the number of digits/characters is limited.

```typescript
function radixSort(arr: number[]): number[] {
  const max = Math.max(...arr);
  let exp = 1;
  
  while (Math.floor(max / exp) > 0) {
    arr = countingSortByDigit(arr, exp);
    exp *= 10;
  }
  
  return arr;
}

function countingSortByDigit(arr: number[], exp: number): number[] {
  const output = Array(arr.length).fill(0);
  const count = Array(10).fill(0);
  
  arr.forEach(num => count[Math.floor(num / exp) % 10]++);
  
  for (let i = 1; i < 10; i++) count[i] += count[i - 1];
  
  for (let i = arr.length - 1; i >= 0; i--) {
    const digit = Math.floor(arr[i] / exp) % 10;
    output[count[digit] - 1] = arr[i];
    count[digit]--;
  }
  
  return output;
}
```

---

## 6. Bucket Sort

### **Type**
- **Distribution Sort**

### **Time Complexity**
- **Average Case**: O(n + k) where *k* is the number of buckets.

### **How It Works**
1. **Distribute Elements**: Place each element into a bucket based on a specific range or hash function.
2. **Sort Buckets**: Individually sort each bucket (can use another sorting algorithm).
3. **Concatenate Buckets**: Combine the sorted buckets to form the final sorted array.

### **Use Case**
- **Uniformly Distributed Data**: Works best when input elements are uniformly distributed across the range.

```typescript
function bucketSort(arr: number[]): number[] {
  const bucketCount = Math.floor(Math.sqrt(arr.length));
  const buckets: number[][] = Array.from({ length: bucketCount }, () => []);
  
  arr.forEach(num => {
    const bucketIndex = Math.floor(num * bucketCount / (Math.max(...arr) + 1));
    buckets[bucketIndex].push(num);
  });
  
  buckets.forEach(bucket => {
    bucket.sort((a, b) => a - b); // Using built-in sort for simplicity
  });
  
  return buckets.flat();
}
```

---

# Quick Recap

- **Lower Bound on Time Complexity**: Sets the efficiency limit for sorting algorithms.
- **Quicksort**: Fast average-case sort using Divide and Conquer; may degrade to O(n²) in the worst case.
- **Merge Sort**: Reliable O(n log n) sort, ideal for stable sorting requirements.
- **Counting Sort**: Efficient for sorting integers with a known, small range.
- **Radix Sort**: Effective for fixed-length numerical or string data by sorting digit by digit.
- **Bucket Sort**: Useful for uniformly distributed data by distributing into and sorting individual buckets.

# Tips for Mastery

- **Understand the Fundamentals**: Grasp how each algorithm sorts data and why it works.
- **Analyze Time Complexity**: Be comfortable calculating and comparing the efficiencies.
- **Practice Implementation**: Write and test each sorting algorithm to reinforce your understanding.
- **Choose Wisely**: Know which algorithm suits different scenarios based on data characteristics and requirements.


---

## Module-IV: Graphs

# Simplified Guide to Graph Algorithms

If you're new to algorithms, understanding graph concepts and algorithms is crucial as they form the backbone of many real-world applications like networking, social media, and route planning. Here's a brief and easy-to-understand overview of essential graph topics and their use cases.

---

## 1. Graph Representations/Storage Implementations

### **Adjacency Matrix**

- **Structure**: A 2D array where each cell `(i, j)` indicates whether there's an edge between vertex `i` and vertex `j`. If the graph is weighted, the cell holds the weight instead of just `1` (indicating presence).
- **Space Complexity**: **O(V²)** where `V` is the number of vertices.
- **Use Case**: Best for **dense graphs** where the number of edges is close to `V²`.

![Adjacency Matrix](https://i.imgur.com/AdTM5YJ.png)

```typescript
const adjacencyMatrix: number[][] = [
  [0, 1, 0],
  [1, 0, 1],
  [0, 1, 0],
];
```

### **Adjacency List**

- **Structure**: An array of lists. Each index represents a vertex, and each list contains the vertices adjacent to it.
- **Space Complexity**: **O(V + E)** where `E` is the number of edges.
- **Use Case**: Ideal for **sparse graphs** with fewer edges.

![Adjacency List](https://i.imgur.com/Z6TfGgw.png)

```typescript
const adjacencyList: number[][] = [
  [1],      // Vertex 0 is connected to Vertex 1
  [0, 2],   // Vertex 1 is connected to Vertex 0 and Vertex 2
  [1],      // Vertex 2 is connected to Vertex 1
];
```

---

## 2. Graph Traversal and Connectivity

### **Depth-First Search (DFS)**

- **Method**: Starts at a source node and explores as far as possible along each branch before backtracking.
- **Applications**: 
  - Detecting cycles
  - Topological sorting
  - Solving puzzles and mazes
- **Implementation**: Can be implemented using **recursion** or a **stack**.

**Use Case Example**: **Detecting a Cycle** in a graph. If during DFS you encounter a previously visited node that is not the parent, a cycle exists.

```typescript
function dfs(vertex: number, visited: boolean[], adjacencyList: number[][]): void {
  visited[vertex] = true;
  adjacencyList[vertex].forEach(neighbor => {
    if (!visited[neighbor]) {
      dfs(neighbor, visited, adjacencyList);
    }
  });
}
```

---

### **Breadth-First Search (BFS)**

- **Method**: Starts at a source node and explores all neighboring nodes at the current depth before moving to nodes at the next depth level.
- **Applications**:
  - Finding the **shortest path** in unweighted graphs
  - Level order traversal
  - Broadcasting in networks
- **Implementation**: Utilizes a **queue**.

**Use Case Example**: **Finding the Shortest Path** between two nodes in an unweighted graph.

```typescript
function bfs(start: number, end: number, adjacencyList: number[][]): number[] | null {
  const queue: number[][] = [[start]];
  const visited: Set<number> = new Set([start]);

  while (queue.length > 0) {
    const path = queue.shift()!;
    const vertex = path[path.length - 1];

    if (vertex === end) return path;

    adjacencyList[vertex].forEach(neighbor => {
      if (!visited.has(neighbor)) {
        visited.add(neighbor);
        queue.push([...path, neighbor]);
      }
    });
  }

  return null; // Path not found
}
```

---

### **Topological Sort**

- **Definition**: A linear ordering of vertices in a Directed Acyclic Graph (DAG) where for every directed edge `uv`, vertex `u` comes before `v`.
- **Applications**:
  - Task scheduling
  - Resolving dependencies in build systems
- **Implementation**: Can be performed using **DFS** or **Kahn’s Algorithm**.

**Use Case Example**: **Task Scheduling** where some tasks must be completed before others.

```typescript
function topologicalSort(adjacencyList: number[][]): number[] {
  const visited: boolean[] = [];
  const stack: number[] = [];

  function dfs(vertex: number) {
    visited[vertex] = true;
    adjacencyList[vertex].forEach(neighbor => {
      if (!visited[neighbor]) dfs(neighbor);
    });
    stack.push(vertex);
  }

  for (let i = 0; i < adjacencyList.length; i++) {
    if (!visited[i]) dfs(i);
  }

  return stack.reverse();
}
```

---

### **Strongly Connected Components (SCC)**

- **Definition**: Maximal subgraphs of a directed graph where every vertex is reachable from every other vertex in the subgraph.
- **Algorithms**: 
  - **Kosaraju’s Algorithm**
  - **Tarjan’s Algorithm**
- **Applications**:
  - Analyzing **network connectivity**
  - Optimizing **compilers**
  
**Use Case Example**: **Analyzing Social Networks** to find groups where everyone is connected to everyone else.

```typescript
// Example using Kosaraju’s Algorithm
function kosarajuSCC(adjacencyList: number[][]): number[][] {
  const V = adjacencyList.length;
  const visited: boolean[] = Array(V).fill(false);
  const stack: number[] = [];

  function fillOrder(v: number) {
    visited[v] = true;
    adjacencyList[v].forEach(neighbor => {
      if (!visited[neighbor]) fillOrder(neighbor);
    });
    stack.push(v);
  }

  for (let i = 0; i < V; i++) {
    if (!visited[i]) fillOrder(i);
  }

  // Transpose the graph
  const transpose: number[][] = Array.from({ length: V }, () => []);
  adjacencyList.forEach((neighbors, v) => {
    neighbors.forEach(neighbor => {
      transpose[neighbor].push(v);
    });
  });

  // DFS on transposed graph
  visited.fill(false);
  const scc: number[][] = [];

  function dfsTranspose(v: number, component: number[]) {
    visited[v] = true;
    component.push(v);
    transpose[v].forEach(neighbor => {
      if (!visited[neighbor]) dfsTranspose(neighbor, component);
    });
  }

  while (stack.length > 0) {
    const v = stack.pop()!;
    if (!visited[v]) {
      const component: number[] = [];
      dfsTranspose(v, component);
      scc.push(component);
    }
  }

  return scc;
}
```

---

## 3. Single-Source Shortest Paths

### **Bellman-Ford Algorithm**

- **Features**:
  - Handles graphs with **negative edge weights**.
  - Detects **negative weight cycles**.
- **Complexity**: **O(V * E)** where `V` is vertices and `E` is edges.
- **Use Case**: Useful in scenarios where some paths might have negative weights, such as financial models involving debts.

```typescript
function bellmanFord(edges: [number, number, number][], V: number, start: number): number[] | null {
  const distance: number[] = Array(V).fill(Infinity);
  distance[start] = 0;

  for (let i = 1; i < V; i++) {
    edges.forEach(([u, v, w]) => {
      if (distance[u] + w < distance[v]) {
        distance[v] = distance[u] + w;
      }
    });
  }

  // Check for negative-weight cycles
  for (let [u, v, w] of edges) {
    if (distance[u] + w < distance[v]) return null; // Negative cycle detected
  }

  return distance;
}
```

### **Dijkstra’s Algorithm**

- **Features**:
  - Efficient for graphs with **non-negative edge weights**.
  - Finds the **shortest path** from a single source to all other vertices.
- **Complexity**: **O(V log V + E)** using a priority queue.
- **Use Case**: Widely used in **routing and navigation systems** like GPS.

```typescript
function dijkstra(adjacencyList: [number, number][][], start: number): number[] {
  const V = adjacencyList.length;
  const distance: number[] = Array(V).fill(Infinity);
  distance[start] = 0;
  const priorityQueue = new MinPriorityQueue({ priority: (x: number) => distance[x] });

  priorityQueue.enqueue(start, distance[start]);

  while (!priorityQueue.isEmpty()) {
    const current = priorityQueue.dequeue().element;
    adjacencyList[current].forEach(([neighbor, weight]) => {
      if (distance[current] + weight < distance[neighbor]) {
        distance[neighbor] = distance[current] + weight;
        priorityQueue.enqueue(neighbor, distance[neighbor]);
      }
    });
  }

  return distance;
}
```

### **Floyd-Warshall Algorithm (All-Pairs Shortest Paths)**

- **Features**:
  - Computes the **shortest paths between all pairs of vertices**.
  - Handles **negative weights**, but not **negative cycles**.
- **Complexity**: **O(V³)**.
- **Use Case**: Suitable for **network routing** and **pathfinding in dense graphs** where you need all possible shortest paths.

```typescript
function floydWarshall(graph: number[][]): number[][] {
  const V = graph.length;
  const dist: number[][] = JSON.parse(JSON.stringify(graph));

  for (let k = 0; k < V; k++) {
    for (let i = 0; i < V; i++) {
      for (let j = 0; j < V; j++) {
        if (dist[i][k] + dist[k][j] < dist[i][j]) {
          dist[i][j] = dist[i][k] + dist[k][j];
        }
      }
    }
  }

  // Check for negative cycles
  for (let i = 0; i < V; i++) {
    if (dist[i][i] < 0) throw new Error("Negative cycle detected");
  }

  return dist;
}
```

---

## 4. Disjoint Set Manipulation

### **UNION - FIND Algorithms**

- **Purpose**: Manage a collection of disjoint (non-overlapping) sets and support two primary operations:
  - **Find**: Determine which subset a particular element is in.
  - **Union**: Merge two subsets into a single subset.
- **Optimizations**:
  - **Path Compression**: Flattens the structure of the tree, making future `Find` operations faster.
  - **Union by Rank**: Attaches the smaller tree under the root of the deeper tree to keep the overall tree shallow.
- **Applications**:
  - Kruskal’s Algorithm for Minimum Spanning Tree
  - Network connectivity
  - Image processing

**Use Case Example**: **Kruskal’s Algorithm** for finding the Minimum Spanning Tree (MST).

```typescript
class DisjointSet {
  parent: number[];
  rank: number[];

  constructor(size: number) {
    this.parent = Array.from({ length: size }, (_, i) => i);
    this.rank = Array(size).fill(0);
  }

  find(u: number): number {
    if (this.parent[u] !== u) {
      this.parent[u] = this.find(this.parent[u]); // Path compression
    }
    return this.parent[u];
  }

  union(u: number, v: number): void {
    const rootU = this.find(u);
    const rootV = this.find(v);

    if (rootU === rootV) return;

    // Union by rank
    if (this.rank[rootU] < this.rank[rootV]) {
      this.parent[rootU] = rootV;
    } else if (this.rank[rootU] > this.rank[rootV]) {
      this.parent[rootV] = rootU;
    } else {
      this.parent[rootV] = rootU;
      this.rank[rootU]++;
    }
  }
}
```

---

## 5. Minimum Spanning Tree (MST)

### **Prim’s Algorithm**

- **Type**: **Greedy**
- **Method**: Starts with a single vertex and **greedily** adds the cheapest possible connection from the tree to another vertex.
- **Complexity**: **O(E + V log V)** using a priority queue.
- **Use Case**: Designing **least-cost networks**, like computer networks or road systems.

```typescript
function primMST(adjacencyList: [number, number][][], V: number): number {
  const selected: boolean[] = Array(V).fill(false);
  const edgeQueue: [number, number][] = [];
  let mstWeight = 0;

  // Start from vertex 0
  selected[0] = true;
  adjacencyList[0].forEach(edge => edgeQueue.push(edge));

  while (edgeQueue.length > 0) {
    // Sort edges by weight
    edgeQueue.sort((a, b) => a[1] - b[1]);
    const [nextVertex, weight] = edgeQueue.shift()!;

    if (!selected[nextVertex]) {
      selected[nextVertex] = true;
      mstWeight += weight;

      adjacencyList[nextVertex].forEach(edge => {
        if (!selected[edge[0]]) edgeQueue.push(edge);
      });
    }
  }

  return mstWeight;
}
```

### **Kruskal’s Algorithm**

- **Type**: **Greedy**
- **Method**: 
  1. **Sorts** all edges in non-decreasing order of their weight.
  2. **Adds** edges one by one, ensuring no cycles are formed using the Union-Find structure.
- **Complexity**: **O(E log E)** due to sorting.
- **Use Case**: Best for **sparse graphs** where the number of edges is much less than `V²`.

```typescript
function kruskalMST(edges: [number, number, number][], V: number): number {
  // Sort edges based on weight
  edges.sort((a, b) => a[2] - b[2]);

  const ds = new DisjointSet(V);
  let mstWeight = 0;

  for (let [u, v, w] of edges) {
    if (ds.find(u) !== ds.find(v)) {
      ds.union(u, v);
      mstWeight += w;
    }
  }

  return mstWeight;
}
```

---

# Quick Recap

- **Adjacency Matrix vs. Adjacency List**: Choose based on graph density—use matrices for dense graphs and lists for sparse ones.
- **DFS vs. BFS**: DFS delves deep, useful for cycle detection; BFS explores level by level, ideal for shortest path in unweighted graphs.
- **Topological Sort**: Order tasks with dependencies, applicable only to DAGs.
- **Strongly Connected Components**: Identify tightly connected subgraphs, useful in network analysis.
- **Shortest Path Algorithms**:
  - **Bellman-Ford**: Handles negative weights.
  - **Dijkstra’s**: Efficient for non-negative weights.
  - **Floyd-Warshall**: Computes all-pairs shortest paths.
- **Disjoint Sets**: Manage and merge disjoint subsets efficiently, crucial for Kruskal’s MST.
- **Minimum Spanning Tree**:
  - **Prim’s**: Good for dense graphs.
  - **Kruskal’s**: Ideal for sparse graphs.

# Tips for Mastery

1. **Visualize**: Draw graphs and visualize traversal methods to better understand how algorithms work.
2. **Implement**: Write code for each algorithm to reinforce your understanding.
3. **Practice Problems**: Solve various graph-related problems to apply what you've learned.
4. **Understand Use Cases**: Knowing where each algorithm is best applied helps in choosing the right one during exams.
5. **Time Complexity**: Be clear about the efficiency of each algorithm and when it’s appropriate to use them based on input size and graph density.


---

# Quick Tips for Your Exam

- **Understand Concepts Thoroughly**: Focus on the underlying principles rather than memorizing steps.
- **Practice Problems**: Apply each algorithm to sample problems to reinforce your understanding.
- **Compare Algorithms**: Know the differences, use-cases, and limitations of each algorithm.
- **Time and Space Analysis**: Be comfortable with calculating and comparing the complexities.
- **Graph Representations**: Be able to convert between adjacency lists and matrices and understand their trade-offs.
- **Algorithm Implementation**: If possible, write pseudocode for key algorithms to solidify your grasp.

Good luck with your exam!

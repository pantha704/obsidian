### Algorithms to Search and Sort

#### 1. Searching Algorithms
Searching algorithms are designed to retrieve information stored within some data structure. The two most common types are linear search and binary search.

##### Linear Search
Linear search is the simplest search algorithm that checks each element in the list until the desired element is found or the list ends.

**Algorithm**:
1. Start from the first element.
2. Compare the current element with the target element.
3. If the current element matches the target, return the index.
4. If the target is not found and the list ends, return -1.

**Example (Python)**:
```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Usage
arr = [1, 2, 3, 4, 5]
print(linear_search(arr, 3))  # Output: 2
```

##### Binary Search
Binary search is more efficient but requires the array to be sorted. It works by repeatedly dividing the search interval in half.

**Algorithm**:
1. Find the middle element.
2. If the middle element is the target, return the index.
3. If the target is less than the middle element, repeat the search in the left half.
4. If the target is greater than the middle element, repeat the search in the right half.
5. If the interval is empty, return -1.

**Example (Python)**:
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Usage
arr = [1, 2, 3, 4, 5]
print(binary_search(arr, 3))  # Output: 2
```

#### 2. Sorting Algorithms
Sorting algorithms arrange elements in a list in a particular order, typically in ascending or descending order. Common sorting algorithms include bubble sort, selection sort, insertion sort, merge sort, quick sort, and heap sort.

##### Bubble Sort
Bubble sort is a simple comparison-based algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

**Algorithm**:
1. Start at the beginning of the list.
2. Compare each pair of adjacent elements.
3. Swap the elements if they are in the wrong order.
4. Repeat the process until the list is sorted.

**Example (Python)**:
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Usage
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print(arr)  # Output: [11, 12, 22, 25, 34, 64, 90]
```

##### Selection Sort
Selection sort divides the list into two parts: the sorted part and the unsorted part. It repeatedly selects the smallest element from the unsorted part and moves it to the end of the sorted part.

**Algorithm**:
1. Find the minimum element in the unsorted part.
2. Swap it with the first element of the unsorted part.
3. Repeat the process for the remaining elements.

**Example (Python)**:
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Usage
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print(arr)  # Output: [11, 12, 22, 25, 64]
```

##### Insertion Sort
Insertion sort builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

**Algorithm**:
1. Start with the first element as the sorted part.
2. Pick the next element and insert it into the sorted part.
3. Repeat until all elements are sorted.

**Example (Python)**:
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Usage
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print(arr)  # Output: [5, 6, 11, 12, 13]
```

##### Merge Sort
Merge sort is an efficient, stable, comparison-based, divide and conquer sorting algorithm. It works by recursively splitting the array into two halves, sorting each half, and merging them back together.

**Algorithm**:
1. Divide the array into two halves.
2. Recursively sort each half.
3. Merge the sorted halves.

**Example (Python)**:
```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Usage
arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
print(arr)  # Output: [5, 6, 7, 11, 12, 13]
```

##### Quick Sort
Quick sort is an efficient, in-place, divide-and-conquer sorting algorithm. It works by selecting a 'pivot' element and partitioning the other elements into two sub-arrays according to whether they are less than or greater than the pivot.

**Algorithm**:
1. Pick a pivot element.
2. Partition the array around the pivot.
3. Recursively apply the above steps to the sub-arrays.

**Example (Python)**:
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Usage
arr = [3, 6, 8, 10, 1, 2, 1]
print(quick_sort(arr))  # Output: [1, 1, 2, 3, 6, 8, 10]
```

These algorithms cover a wide range of searching and sorting techniques, suitable for various scenarios and performance requirements.
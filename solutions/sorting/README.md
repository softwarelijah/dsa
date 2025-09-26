# Sorting Algorithms - Complete Guide

## Overview
This guide covers various sorting algorithms with their time and space complexities, implementations, and use cases.

## Table of Contents
1. [Bubble Sort](#bubble-sort)
2. [Insertion Sort](#insertion-sort)
3. [Selection Sort](#selection-sort)
4. [Merge Sort](#merge-sort)
5. [Quick Sort](#quick-sort)
6. [Counting Sort](#counting-sort)
7. [Built-in Python Sorting](#built-in-python-sorting)
8. [Advanced Sorting Techniques](#advanced-sorting-techniques)

---

## Bubble Sort

### Concept
Creates a "bubbling effect" where elements fall into their correct positions by repeatedly comparing adjacent elements and swapping them if they're in the wrong order.

### Algorithm Steps
1. Place index `i` at position 1
2. Compare elements at positions `i` and `i-1`
3. Swap if left element is greater than right element (for ascending order)
4. Increment `i` and repeat until end of array
5. Repeat entire process until no swaps are needed

### Time & Space Complexity
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1) - in-place sorting

### Implementation
```python
def bubble_sort(array):
    n = len(array)
    flag = True  # Flag to track if swaps occurred
    
    while flag:
        flag = False  # Assume we're done
        
        for i in range(1, n):
            if array[i-1] > array[i]:
                # Swap elements
                array[i-1], array[i] = array[i], array[i-1]
                flag = True  # We made a swap, so continue
```

---

## Insertion Sort

### Concept
Maintains a sorted portion of the array and inserts elements from the unsorted portion into their correct position in the sorted portion.

### Algorithm Steps
1. Start with first element as "sorted portion"
2. Take next element from unsorted portion
3. Find correct position in sorted portion
4. Insert element at correct position
5. Repeat until all elements are processed

### Time & Space Complexity
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1) - in-place sorting

### Implementation
```python
def insertion_sort(array):
    n = len(array)
    
    for i in range(1, n):
        # Go backwards through sorted portion
        for j in range(i, 0, -1):
            if array[j-1] > array[j]:
                # Swap elements
                array[j-1], array[j] = array[j], array[j-1]
            else:
                # Found correct position, stop
                break
```

---

## Selection Sort

### Concept
Repeatedly finds the minimum element from the unsorted portion and places it at the beginning of the unsorted portion.

### Algorithm Steps
1. Find minimum element in entire array
2. Swap with first element
3. Find minimum in remaining unsorted portion
4. Swap with first element of unsorted portion
5. Repeat until array is sorted

### Time & Space Complexity
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1) - in-place sorting

### Implementation
```python
def selection_sort(array):
    n = len(array)
    
    for i in range(n):
        min_index = i
        
        # Find minimum in remaining array
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        
        # Swap with current position
        array[i], array[min_index] = array[min_index], array[i]
```

---

## Merge Sort

### Concept
Divide and conquer algorithm that recursively splits the array into halves until single elements, then merges them back in sorted order.

### Algorithm Steps
1. **Divide:** Split array into two halves at midpoint
2. **Conquer:** Recursively sort both halves
3. **Merge:** Combine sorted halves into single sorted array

### Time & Space Complexity
- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n) - requires additional space for merging

### Key Insights
- Tree height is log₂(n) due to halving at each level
- Each level processes O(n) elements
- Total: O(n) × O(log n) = O(n log n)

### Implementation
```python
def merge_sort(array):
    n = len(array)
    
    # Base case
    if n <= 1:
        return array
    
    # Divide
    m = n // 2
    left = array[:m]
    right = array[m:]
    
    # Conquer (recursively sort)
    left = merge_sort(left)
    right = merge_sort(right)
    
    # Merge
    sorted_array = [0] * n
    l = r = i = 0
    left_len = len(left)
    right_len = len(right)
    
    # Merge while both arrays have elements
    while l < left_len and r < right_len:
        if left[l] <= right[r]:
            sorted_array[i] = left[l]
            l += 1
        else:
            sorted_array[i] = right[r]
            r += 1
        i += 1
    
    # Add remaining elements
    while l < left_len:
        sorted_array[i] = left[l]
        l += 1
        i += 1
    
    while r < right_len:
        sorted_array[i] = right[r]
        r += 1
        i += 1
    
    return sorted_array
```

---

## Quick Sort

### Concept
Divide and conquer algorithm that selects a pivot element and partitions the array around it, then recursively sorts the partitions.

### Algorithm Steps
1. Choose pivot (typically last element)
2. Partition array into three parts:
    - Elements ≤ pivot (left)
    - Pivot element (middle)
    - Elements > pivot (right)
3. Recursively sort left and right partitions
4. Concatenate: left + pivot + right

### Time & Space Complexity
- **Average Time Complexity:** O(n log n)
- **Worst Time Complexity:** O(n²) - occurs with bad pivot selection
- **Space Complexity:** O(log n) minimum, O(n) for our implementation

### Implementation
```python
def quick_sort(array):
    # Base case
    if len(array) <= 1:
        return array
    
    # Choose pivot (last element)
    pivot = array[-1]
    
    # Partition
    left = [x for x in array[:-1] if x <= pivot]
    right = [x for x in array[:-1] if x > pivot]
    
    # Recursively sort and combine
    return quick_sort(left) + [pivot] + quick_sort(right)
```

---

## Counting Sort

### Concept
Non-comparison based sorting algorithm that works by counting occurrences of each distinct element, then using this information to place elements in sorted order.

### Algorithm Steps
1. Find maximum value in array
2. Create counts array of size (max + 1)
3. Count occurrences of each value
4. Use counts to overwrite original array in sorted order

### Time & Space Complexity
- **Time Complexity:** O(n + k) where k is the range of input
- **Space Complexity:** O(k)

### When to Use
- When k (range of values) is small
- With non-negative integers
- Can be adapted for negative numbers with additional complexity

### Implementation
```python
def counting_sort(array):
    n = len(array)
    max_val = max(array)
    
    # Initialize counts array
    counts = [0] * (max_val + 1)
    
    # Count occurrences
    for num in array:
        counts[num] += 1
    
    # Reconstruct sorted array
    i = 0
    for c in range(max_val + 1):
        while counts[c] > 0:
            array[i] = c
            i += 1
            counts[c] -= 1
```

---

## Built-in Python Sorting

Python provides efficient built-in sorting methods using Timsort algorithm (O(n log n)).

### In-place Sorting
```python
# Modifies original array
array.sort()

# Reverse order
array.sort(reverse=True)
```

### Creating New Sorted Array
```python
# Returns new sorted array, original unchanged
sorted_array = sorted(array)

# Reverse order
sorted_array = sorted(array, reverse=True)
```

---

## Advanced Sorting Techniques

### Sorting Tuples/Complex Objects

You can sort arrays of tuples using custom key functions:

```python
# Array of tuples
tuples_array = [(-5, 3), (2, 1), (-3, 3), (7, 2), (2, 2)]

# Sort by first element
sorted_by_first = sorted(tuples_array, key=lambda t: t[0])

# Sort by second element
sorted_by_second = sorted(tuples_array, key=lambda t: t[1])

# Sort by second element in reverse
sorted_reverse = sorted(tuples_array, key=lambda t: -t[1])
```

### Common Use Cases
- **Intervals problems:** Often require sorting by start or end times
- **Custom objects:** Sort by specific attributes
- **Multiple criteria:** Can combine multiple sorting keys

---

## Algorithm Comparison

| Algorithm | Time (Best) | Time (Average) | Time (Worst) | Space | Stable | In-place |
|-----------|-------------|----------------|--------------|-------|---------|----------|
| Bubble | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| Selection | O(n²) | O(n²) | O(n²) | O(1) | No | Yes |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | No |
| Quick | O(n log n) | O(n log n) | O(n²) | O(log n) | No | Yes* |
| Counting | O(n + k) | O(n + k) | O(n + k) | O(k) | Yes | No |

*Quick sort can be implemented in-place with more complex partitioning

---

## When to Use Each Algorithm

- **Bubble/Insertion/Selection:** Educational purposes, very small datasets
- **Merge Sort:** When stable sorting is required, consistent O(n log n) performance
- **Quick Sort:** General purpose, average case performance, in-place sorting
- **Counting Sort:** Small range of integers, need linear time complexity
- **Python's built-in:** Production code, most practical applications
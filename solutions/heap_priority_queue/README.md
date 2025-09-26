# Heaps and Priority Queues - Complete Guide

## Overview

**Heaps** and **Priority Queues** are essentially the same data structure. Whether someone says "heap" or "priority queue," they're referring to the same thing.

A heap is a particular type of **binary tree** with special properties that make it efficient for finding minimum or maximum values.

## Key Concepts

### What is a Heap?

A heap is a binary tree that satisfies the **heap property**:
- **Min Heap**: Parent nodes are smaller than their children (root contains minimum)
- **Max Heap**: Parent nodes are larger than their children (root contains maximum)

### Array Representation

Heaps are typically represented as arrays where:
- Root is at index 0
- For any index `i`:
    - Left child: `2 * i + 1`
    - Right child: `2 * i + 2`
    - Parent: `(i - 1) // 2`

## Core Operations

### 1. Heapify
**Purpose**: Convert an arbitrary binary tree into a heap
- **Time Complexity**: O(n)
- **Space Complexity**: O(1) - can be done in place

### 2. Heap Push (Insert)
**Purpose**: Insert a new element into the heap
- **Time Complexity**: O(log n)
- **Process**: Add element at end, then "bubble up" to correct position

### 3. Heap Pop (Extract Min/Max)
**Purpose**: Remove and return the root element (min/max)
- **Time Complexity**: O(log n)
- **Process**: Remove root, move last element to root, then "sift down"

### 4. Heap Peek
**Purpose**: View the root element without removing it
- **Time Complexity**: O(1)
- **Implementation**: Simply return `array[0]`

## Python Implementation (using heapq)

### Basic Setup

```python
import heapq

# Create a heap from existing array
arr = [3, 1, 6, 5, 2, 4]
heapq.heapify(arr)  # Converts to min heap in-place
print(arr)  # [1, 2, 4, 5, 6, 3]
```

### Min Heap Operations

```python
# Initialize empty heap
heap = []

# Push elements
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)

# Pop minimum element
min_element = heapq.heappop(heap)  # Returns 1

# Peek at minimum (without removing)
if heap:
    min_value = heap[0]

# Push and pop in one operation
result = heapq.heappushpop(heap, 5)  # Push 5, then pop min

# Get heap size
size = len(heap)
```

### Max Heap (Workaround)

Since `heapq` only supports min heaps, create max heap by negating values:

```python
# Max heap implementation
max_heap = []
values = [3, 1, 6, 5, 2, 4]

# Convert to max heap by negating values
for val in values:
    heapq.heappush(max_heap, -val)

# Pop maximum (negate result)
max_element = -heapq.heappop(max_heap)  # Returns 6

# Push into max heap
heapq.heappush(max_heap, -7)  # Inserts 7 into max heap
```

## Heap Sort Algorithm

Heap Sort uses heap operations to sort an array:

```python
def heap_sort(array):
    """
    Sorts array using heap sort algorithm
    Time Complexity: O(n log n)
    Space Complexity: O(n) - this version creates new array
    """
    # Convert to heap
    heapq.heapify(array)
    
    n = len(array)
    sorted_list = [0] * n
    
    # Repeatedly extract minimum
    for i in range(n):
        sorted_list[i] = heapq.heappop(array)
    
    return sorted_list

# Example usage
unsorted = [3, 6, 8, 10, 1, 2, 1]
sorted_array = heap_sort(unsorted.copy())
print(sorted_array)  # [1, 1, 2, 3, 6, 8, 10]
```

## Priority Queues with Custom Objects

Use tuples to store priority and data together:

```python
# Priority queue with (priority, data) tuples
priority_queue = []

# Add items (lower number = higher priority)
heapq.heappush(priority_queue, (1, "High priority task"))
heapq.heappush(priority_queue, (3, "Low priority task"))
heapq.heappush(priority_queue, (2, "Medium priority task"))

# Process items by priority
while priority_queue:
    priority, task = heapq.heappop(priority_queue)
    print(f"Processing: {task} (priority: {priority})")
```

## Working with Frequency Counting

Common pattern for LeetCode problems:

```python
from collections import Counter

# Count frequencies
data = [5, 5, 5, 5, 4, 4, 4, 3, 3]
counter = Counter(data)

# Create heap of (frequency, element) pairs
heap = []
for element, frequency in counter.items():
    heapq.heappush(heap, (frequency, element))

print(heap)  # [(2, 3), (3, 4), (4, 5)]

# Now you can process elements by frequency
while heap:
    freq, element = heapq.heappop(heap)
    print(f"Element {element} appears {freq} times")
```

## Time Complexity Summary

| Operation | Time Complexity | Description |
|-----------|----------------|-------------|
| Heapify | O(n) | Convert array to heap |
| Push | O(log n) | Insert element |
| Pop | O(log n) | Extract min/max |
| Peek | O(1) | View root element |
| Build from scratch | O(n log n) | Push n elements one by one |

## Space Complexity

- **Heapify existing array**: O(1) - in-place
- **Creating new heap**: O(n)
- **Heap Sort (this version)**: O(n) - creates new array

## Key Benefits

1. **Efficient priority operations**: Always access min/max in O(1)
2. **Dynamic**: Can insert/remove elements efficiently
3. **Memory efficient**: Array representation
4. **Versatile**: Works with custom priorities and objects

## Common Use Cases

- **Dijkstra's algorithm** (shortest path)
- **A* search algorithm**
- **Task scheduling** with priorities
- **Finding k largest/smallest elements**
- **Merge k sorted lists**
- **Median maintenance**

## Important Notes

- Python's `heapq` only supports **min heaps**
- For max heaps, negate values when pushing/popping
- Heap property: parent ≤ children (min heap) or parent ≥ children (max heap)
- **Not fully sorted** - only guarantees root is min/max
- Heaps are **complete binary trees** (filled left to right)

## Tips for Coding Interviews

1. Remember to import `heapq`
2. Use tuples for priority queues: `(priority, data)`
3. For max heap, negate numeric values
4. Always check if heap is empty before peeking: `if heap:`
5. Heap sort is O(n log n) - one of the best sorting algorithms
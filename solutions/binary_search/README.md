# Binary Search Algorithm

## Overview
Binary search is an efficient algorithm for finding a target value in a sorted array. It works by repeatedly dividing the search space in half, eliminating half of the remaining elements at each step.

## Two Methods Covered

### 1. Traditional Binary Search
Searches for a specific number in a sorted array.

### 2. Over/Under Technique (Condition-Based)
Finds the first occurrence where a condition changes from false to true (or vice versa).

---

## Traditional Binary Search

### Problem
Given a sorted array of integers, determine if a target value exists in the array.

### Algorithm Steps
1. Initialize two pointers: `left = 0`, `right = n - 1`
2. While `left <= right`:
    - Calculate middle index: `mid = left + (right - left) // 2`
    - If `array[mid] == target`: return `True`
    - If `target < array[mid]`: search left half → `right = mid - 1`
    - If `target > array[mid]`: search right half → `left = mid + 1`
3. If loop ends without finding target: return `False`

### Python Implementation
```python
def binary_search(arr, target):
    n = len(arr)
    left = 0
    right = n - 1
    
    while left <= right:
        # Avoid integer overflow (preferred formula)
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return True
        elif target < arr[mid]:
            right = mid - 1  # Search left half
        else:
            left = mid + 1   # Search right half
    
    return False
```

### Alternative Mid Calculation
```python
# Simple method (can cause overflow in some languages)
mid = (left + right) // 2

# Preferred method (avoids overflow)
mid = left + (right - left) // 2
```

---

## Condition-Based Binary Search (Over/Under Technique)

### Problem
Find the first position where a condition changes from `False` to `True` in a boolean array arranged like: `[False, False, ..., True, True, ...]`

### Algorithm Steps
1. Initialize: `left = 0`, `right = n - 1`
2. While `left < right` (note: not `<=`):
    - Calculate `mid = (left + right) // 2`
    - If condition at `mid` is `True`:
        - We might be at the first `True` or there might be earlier ones
        - Search left half: `right = mid` (keep mid as possibility)
    - If condition at `mid` is `False`:
        - First `True` must be to the right
        - Search right half: `left = mid + 1`
3. Return `left` (or `right`, they're equal when loop ends)

### Python Implementation
```python
def binary_search_condition(arr):
    n = len(arr)
    left = 0
    right = n - 1
    
    while left < right:  # Note: < not <=
        mid = (left + right) // 2
        
        if arr[mid]:  # If condition is True
            right = mid      # Keep mid as possibility
        else:         # If condition is False
            left = mid + 1   # Move past mid
    
    return left  # or return right (they're equal)
```

---

## Time and Space Complexity

### Time Complexity: O(log n)
- Each iteration eliminates half of the search space
- For array of size n: n → n/2 → n/4 → n/8 → ... → 1
- Number of steps = log₂(n)

### Space Complexity: O(1)
- Only uses a constant amount of extra space
- Variables: `left`, `right`, `mid`
- Iterative approach (no recursion stack)

---

## Key Differences Between Methods

| Aspect | Traditional | Condition-Based |
|--------|-------------|-----------------|
| Loop Condition | `left <= right` | `left < right` |
| Target | Specific value | First occurrence of condition |
| Return | `True`/`False` | Index position |
| Right Update | `right = mid - 1` | `right = mid` |

---

## Important Notes

### Why `left < right` in Condition-Based?
- The algorithm stops when `left == right`
- At this point, both pointers are at the answer
- Using `<=` would cause infinite loop

### Why `right = mid` (not `mid - 1`)?
- When we find a `True`, it might be the first one
- We can't eliminate it from consideration
- We keep it as a possibility while searching left

### Integer Overflow Prevention
```python
# Can overflow in some languages
mid = (left + right) // 2

# Safer approach
mid = left + (right - left) // 2
```

---

## Example Walkthrough

### Traditional Search
Array: `[-3, -1, 0, 1, 4, 7]`, Target: `1`

1. `left=0, right=5, mid=2` → `arr[2]=0 < 1` → `left=3`
2. `left=3, right=5, mid=4` → `arr[4]=4 > 1` → `right=3`
3. `left=3, right=3, mid=3` → `arr[3]=1 == 1` → **Found!**

### Condition-Based Search
Array: `[False, False, False, True, True, True]`

1. `left=0, right=5, mid=2` → `arr[2]=False` → `left=3`
2. `left=3, right=5, mid=4` → `arr[4]=True` → `right=4`
3. `left=3, right=4, mid=3` → `arr[3]=True` → `right=3`
4. `left=3, right=3` → **Stop! First True is at index 3**

---

## Applications

### Traditional Binary Search
- Finding elements in sorted arrays
- Dictionary lookups
- Database queries

### Condition-Based Binary Search
- Finding insertion points
- LeetCode problems involving "first/last occurrence"
- Peak finding problems
- Rotated array searches

---

## Practice Tips
1. **Memorize the traditional implementation** - you'll write it frequently
2. **Understand the loop conditions** - `<=` vs `<` is crucial
3. **Practice both pointer update strategies** - when to use `mid±1` vs `mid`
4. **Remember overflow prevention** - use `left + (right-left)//2`
5. **Test edge cases** - empty arrays, single elements, not found scenarios
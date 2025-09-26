# Two Pointers Algorithm

## Overview

The **Two Pointers** technique is a fundamental algorithm pattern that uses two indices (often called "pointers") to traverse an array or data structure efficiently. Despite the name "pointers," we're actually working with array indices.

### Common Patterns

1. **Squeeze Pattern** (Most Common):
    - One pointer starts at the beginning (`left`)
    - One pointer starts at the end (`right`)
    - Pointers move toward each other until they meet

2. **Sliding Window Pattern**:
    - Both pointers start at the beginning
    - They slide across the array together

## Problem: Squares of a Sorted Array

### Problem Statement
Given an integer array `nums` sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

**Example:**
```
Input: [-4, -1, 0, 3, 10]
Output: [0, 1, 9, 16, 100]
```

### Why This Problem is Tricky
- Original array is sorted: `[-4, -1, 0, 3, 10]`
- After squaring: `[16, 1, 0, 9, 100]` (no longer sorted!)
- We need to sort the squared values efficiently

### Approach 1: Brute Force
```python
def sortedSquares_bruteforce(nums):
    result = [x * x for x in nums]
    result.sort()
    return result
```
- **Time Complexity:** O(n log n) - due to sorting
- **Space Complexity:** O(1) - if we don't count the result array

### Approach 2: Two Pointers (Optimal)

#### Key Insight
After squaring, the largest values will always be at the **outer edges** of the array (leftmost or rightmost positions).

#### Algorithm Steps
1. Initialize two pointers: `left = 0`, `right = len(nums) - 1`
2. Create result array
3. Compare absolute values at both pointers
4. Take the larger squared value and add to result
5. Move the corresponding pointer toward center
6. Continue until pointers cross
7. Reverse the result array

#### Code Implementation
```python
def sortedSquares(nums):
    left = 0
    right = len(nums) - 1
    result = []
    
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result.append(nums[left] * nums[left])
            left += 1
        else:
            result.append(nums[right] * nums[right])
            right -= 1
    
    # Reverse because we built array in descending order
    result.reverse()
    return result
```

#### Step-by-Step Example
```
Original: [-4, -1, 0, 3, 10]
Squared:  [16,  1, 0, 9, 100]

Step 1: left=0, right=4
        abs(-4)=4 vs abs(10)=10 → take 10² = 100
        result = [100], right = 3

Step 2: left=0, right=3  
        abs(-4)=4 vs abs(3)=3 → take (-4)² = 16
        result = [100, 16], left = 1

Step 3: left=1, right=3
        abs(-1)=1 vs abs(3)=3 → take 3² = 9
        result = [100, 16, 9], right = 2

Step 4: left=1, right=2
        abs(-1)=1 vs abs(0)=0 → take (-1)² = 1
        result = [100, 16, 9, 1], left = 2

Step 5: left=2, right=2
        Only 0 remains → take 0² = 0
        result = [100, 16, 9, 1, 0]

Final: Reverse → [0, 1, 9, 16, 100]
```

## Complexity Analysis

### Time Complexity: O(n)
- Single pass through the array with two pointers
- Reversing the array takes O(n) time
- Total: O(n) + O(n) = O(n)

### Space Complexity: O(1)
- Only using the result array (which is required for output)
- No additional space used beyond what's needed for the answer

## Key Takeaways

1. **Two pointers** is excellent for problems involving sorted arrays
2. The **squeeze pattern** works when you need to find pairs or compare elements from opposite ends
3. Sometimes building the result in reverse order is more efficient
4. Always consider the termination condition: typically when `left > right`
5. This technique often reduces time complexity from O(n²) or O(n log n) to O(n)

## When to Use Two Pointers

- Array/string problems involving pairs or subsequences
- Finding elements that sum to a target
- Reversing or rearranging elements
- Problems where you need to compare elements from different positions
- Optimization problems on sorted arrays
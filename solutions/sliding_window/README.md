# Sliding Window Algorithm

## Overview

The sliding window technique is a popular algorithmic pattern used to solve problems involving arrays or strings where you need to examine contiguous subarrays or substrings.

## Types of Sliding Window

### 1. Variable Length Sliding Window
- Window size can change dynamically
- Expands and contracts based on conditions

### 2. Fixed Length Sliding Window
- Window has a fixed size (often given as parameter K)
- Window slides across the array maintaining constant size

## When to Use Sliding Window

**Key Indicators:**
- Problems involving **subarrays** (for arrays) or **substrings** (for strings)
- Need to find contiguous sequences
- Optimization problems (longest, shortest, maximum, minimum)

⚠️ **Note:** Subarray/substring = contiguous elements, Subsequence = non-contiguous elements

## Variable Length Sliding Window

### Problem Example: Longest Substring Without Repeating Characters (LeetCode #3)

**Problem:** Given a string `s`, find the length of the longest substring without repeating characters.

**Example:** `"abcabcbb"` → Output: `3` (substring "abc")

### Algorithm Approach

1. Use two pointers: `L` (left) and `R` (right)
2. Use a set to track characters in current window
3. **Window Validity Rule:** No duplicate characters

### Step-by-Step Process

1. **Expand window:** Move `R` right while window is valid
2. **Contract window:** Move `L` right when window becomes invalid
3. **Track maximum:** Update longest length when window is valid

### Code Implementation

```python
def lengthOfLongestSubstring(s):
    L = 0
    longest = 0
    char_set = set()
    n = len(s)
    
    for R in range(n):
        # While window is invalid (duplicate found)
        while s[R] in char_set:
            char_set.remove(s[L])
            L += 1
        
        # Window is now valid
        char_set.add(s[R])
        window_length = R - L + 1
        longest = max(longest, window_length)
    
    return longest
```

### Time & Space Complexity
- **Time:** O(n) - each character visited at most twice
- **Space:** O(n) - for the character set

## Fixed Length Sliding Window

### Problem Example: Maximum Average Subarray (LeetCode #643)

**Problem:** Given array `nums` and integer `k`, find contiguous subarray of length `k` with maximum average.

**Example:** `nums = [1,12,-5,-6,50,3]`, `k = 4` → Output: `12.75`

### Algorithm Approach

1. **Build initial window:** Calculate sum of first `k` elements
2. **Slide window:** Add new element, remove old element
3. **Track maximum:** Keep track of maximum average seen

### Step-by-Step Process

1. **Phase 1 - Build Window:** Sum first `k` elements
2. **Phase 2 - Slide Window:** For each subsequent position:
    - Add `nums[i]` (new right element)
    - Subtract `nums[i-k]` (old left element)
    - Calculate new average and update maximum

### Code Implementation

```python
def findMaxAverage(nums, k):
    n = len(nums)
    
    # Build initial window
    current_sum = 0
    for i in range(k):
        current_sum += nums[i]
    
    max_average = current_sum / k
    
    # Slide window
    for i in range(k, n):
        current_sum += nums[i]        # Add new element
        current_sum -= nums[i - k]    # Remove old element
        current_average = current_sum / k
        max_average = max(max_average, current_average)
    
    return max_average
```

### Time & Space Complexity
- **Time:** O(n) - single pass through array
- **Space:** O(1) - constant space

## Key Formulas

### Window Length Calculation
```python
window_length = R - L + 1
```
Where `R` is right pointer, `L` is left pointer

### Sliding Window Element Management
```python
# Add new element (expanding right)
current_sum += nums[R]

# Remove old element (contracting left)  
current_sum -= nums[L]
```

## General Template

### Variable Length Template
```python
def sliding_window_variable(arr):
    L = 0
    result = 0
    window_data = {}  # Could be set, dict, etc.
    
    for R in range(len(arr)):
        # Add arr[R] to window
        # Update window_data
        
        # While window is invalid
        while window_invalid_condition:
            # Remove arr[L] from window
            # Update window_data
            L += 1
        
        # Window is valid, update result
        result = max(result, R - L + 1)
    
    return result
```

### Fixed Length Template
```python
def sliding_window_fixed(arr, k):
    # Build initial window
    window_sum = sum(arr[:k])
    result = window_sum
    
    # Slide window
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        result = max(result, window_sum)
    
    return result
```

## Practice Problems

### Variable Length
- Longest Substring Without Repeating Characters (LC #3)
- Minimum Window Substring (LC #76)
- Longest Substring with At Most K Distinct Characters

### Fixed Length
- Maximum Average Subarray I (LC #643)
- Maximum Sum of Distinct Subarrays With Length K
- Sliding Window Maximum (LC #239)

## Tips & Tricks

1. **Always ask:** "Is my current window valid?"
2. **Two-pointer approach:** Left contracts, right expands
3. **Use appropriate data structures:** Set for duplicates, HashMap for frequency
4. **Window length formula:** `R - L + 1`
5. **Time complexity:** Usually O(n) because each element visited at most twice

---

*Remember: Sliding window is about maintaining a "window" of elements and efficiently updating it as you traverse the data structure.*
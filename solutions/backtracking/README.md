# Recursive Backtracking

## Overview

Recursive backtracking is a **brute force technique** that uses recursion to exhaustively search through all possible solutions. It's characterized by:

- Making decisions
- Moving forward with recursion
- Undoing decisions when backtracking
- Exploring all possible paths

## Key Concept

The core idea is: **make decisions → recurse → undo decisions**

This technique is ideal when you need to find **all solutions** to a problem (look for keywords like "all subsets", "all permutations", etc.).

## Example: Subsets Problem

**Problem**: Given an integer array `nums` of unique elements, return all possible subsets (the power set).

**Input**: `[1, 2, 3]`
**Output**: `[[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]`

### Mathematical Foundation
- For n elements, there are 2^n possible subsets
- For each element, we have 2 choices: include it or exclude it
- Example: 3 elements → 2³ = 8 subsets

## Decision Tree Visualization

```
                    []
                   /  \
            (don't pick 1)  (pick 1)
                 /              \
               []                [1]
              /  \              /   \
       (don't pick 2) (pick 2) (don't pick 2) (pick 2)
           /        \      /         \        /        \
         []         [2]   [1]      [1,2]   ...       ...
        / \        / \   / \       / \
      []  [3]    [2] [2,3] [1] [1,3] [1,2] [1,2,3]
```

## Algorithm Template

### Standard Structure
```python
def backtrack_solution(nums):
    n = len(nums)
    result = []  # Stores all solutions
    solution = []  # Current partial solution
    
    def backtrack(index):
        # Base case: reached end of array
        if index == n:
            result.append(solution.copy())  # Important: use copy!
            return
        
        # Path 1: Don't pick current element
        backtrack(index + 1)
        
        # Path 2: Pick current element
        solution.append(nums[index])  # Make decision
        backtrack(index + 1)          # Recurse
        solution.pop()                # Undo decision (backtrack)
    
    backtrack(0)
    return result
```

### Complete Subsets Solution
```python
def subsets(nums):
    n = len(nums)
    res = []
    sol = []
    
    def backtrack(i):
        if i == n:
            res.append(sol.copy())
            return
        
        # Don't pick nums[i]
        backtrack(i + 1)
        
        # Pick nums[i]
        sol.append(nums[i])
        backtrack(i + 1)
        sol.pop()
    
    backtrack(0)
    return res
```

## Key Implementation Points

1. **Use `solution.copy()`**: Never append `solution` directly to results - it's a reference that changes
2. **Global variables**: `result` and `solution` are typically global to the recursive function
3. **Three steps for picking**: append → recurse → pop
4. **Base case**: Usually when index goes out of bounds

## Traversal Order (DFS)

The algorithm performs a depth-first search through the decision tree:
1. Goes left first (don't pick)
2. Hits base case, adds solution
3. Backtracks and goes right (pick)
4. Continues this pattern recursively

## Complexity Analysis

### Time Complexity: O(2^n)
- Each level of the tree doubles the number of nodes
- Level 0: 2⁰ = 1 node
- Level 1: 2¹ = 2 nodes
- Level 2: 2² = 4 nodes
- Level n: 2ⁿ nodes

### Space Complexity: O(n)
- Due to the recursive call stack depth
- Maximum recursion depth is n (the length of input array)
- Note: The result storage is not counted as "extra" space since it's part of the output

## When to Use Recursive Backtracking

- Finding **all** solutions to a problem
- Problems involving combinations, permutations, subsets
- Constraint satisfaction problems
- Puzzle solving (N-Queens, Sudoku, etc.)
- Path finding with constraints

## Common Patterns

1. **Generate all subsets/combinations**
2. **Generate all permutations**
3. **Solve constraint satisfaction problems**
4. **Find all valid paths/arrangements**

Remember: If you see "all" in the problem statement, think recursive backtracking!
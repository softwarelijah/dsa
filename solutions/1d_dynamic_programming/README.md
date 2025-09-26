# Dynamic Programming - Complete Guide

## Overview
Dynamic Programming (DP) is an algorithmic technique for solving optimization problems by breaking them down into simpler subproblems. It's particularly useful when the problem has overlapping subproblems and optimal substructure.

## Four Steps of Dynamic Programming

### 1. Naive Recursive Solution
- Start by writing a simple recursive solution
- Don't worry about optimization initially
- This might have poor time complexity (O(2^n), O(3^n), or O(n!))
- Example: Direct implementation of mathematical definition

### 2. Top-Down DP (Memoization)
- Apply caching to the recursive solution
- Use a hash map/dictionary to store computed results
- Still uses recursion but avoids redundant calculations
- **Memoization = Memory + Optimization**

### 3. Bottom-Up DP (Tabulation)
- Convert recursive approach to iterative using loops
- Fill out a table/array from base cases upward
- Generally faster than top-down approach
- Most programming languages handle loops better than recursion

### 4. Space Optimization (if possible)
- Reduce space complexity to O(1) when possible
- Use variables instead of arrays
- Identify what previous states are actually needed

## Example: Fibonacci Numbers (LeetCode #509)

### Problem Definition
The Fibonacci sequence is defined as:
- F(0) = 0
- F(1) = 1
- F(n) = F(n-1) + F(n-2) for n > 1

### Step 1: Naive Recursive Solution

```python
def fib(self, n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return self.fib(n-2) + self.fib(n-1)
```

**Time Complexity:** O(2^n) - exponential
**Space Complexity:** O(n) - recursion stack
**Problem:** Overlapping subproblems cause redundant calculations

### Step 2: Top-Down DP (Memoization)

```python
def fib(self, n):
    memo = {0: 0, 1: 1}  # Base cases
    
    def f(x):
        if x in memo:
            return memo[x]
        memo[x] = f(x-1) + f(x-2)
        return memo[x]
    
    return f(n)
```

**Time Complexity:** O(n) - each subproblem computed once
**Space Complexity:** O(n) - memo dictionary + recursion stack

### Step 3: Bottom-Up DP (Tabulation)

```python
def fib(self, n):
    if n == 0: return 0
    if n == 1: return 1
    
    dp = [0] * (n + 1)  # Create table
    dp[0] = 0  # Base cases
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-2] + dp[i-1]
    
    return dp[n]
```

**Time Complexity:** O(n) - single loop through n elements
**Space Complexity:** O(n) - DP table storage

### Step 4: Space Optimized Bottom-Up

```python
def fib(self, n):
    if n == 0: return 0
    if n == 1: return 1
    
    prev, curr = 0, 1
    
    for i in range(2, n + 1):
        prev, curr = curr, prev + curr
    
    return curr
```

**Time Complexity:** O(n) - single loop
**Space Complexity:** O(1) - only two variables needed

## Key Concepts

### Overlapping Subproblems
- Same subproblems are solved multiple times in naive recursion
- Example: Computing F(4) multiple times when calculating F(6)
- Memoization eliminates redundant calculations

### Optimal Substructure
- Optimal solution contains optimal solutions to subproblems
- Fibonacci: F(n) depends on optimal solutions F(n-1) and F(n-2)

### Top-Down vs Bottom-Up

| Aspect | Top-Down (Memoization) | Bottom-Up (Tabulation) |
|--------|------------------------|------------------------|
| Implementation | Recursive with cache | Iterative with table |
| Direction | Problem → Base cases | Base cases → Problem |
| Space | Recursion stack + memo | Table only |
| Performance | Slightly slower | Generally faster |
| Intuition | Natural problem flow | Build solution step by step |

## When to Use Each Approach

### Use Top-Down (Memoization) when:
- Recursive solution feels natural
- Not all subproblems need to be solved
- Problem has clear recursive structure

### Use Bottom-Up (Tabulation) when:
- Want to avoid recursion overhead
- Need to solve all subproblems anyway
- Memory usage is a concern
- Want optimal performance

## General DP Problem-Solving Strategy

1. **Identify if it's a DP problem:**
    - Optimal substructure present
    - Overlapping subproblems exist
    - Can be broken into similar smaller problems

2. **Define the state:**
    - What parameters uniquely identify a subproblem?
    - What does dp[i] represent?

3. **Find the recurrence relation:**
    - How does current state relate to previous states?
    - What are the base cases?

4. **Choose implementation approach:**
    - Start with memoization if recursion feels natural
    - Convert to tabulation for better performance
    - Optimize space if possible

## Time and Space Complexity Summary

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Naive Recursive | O(2^n) | O(n) | Exponential, avoid in practice |
| Memoization | O(n) | O(n) | Recursion + memo overhead |
| Tabulation | O(n) | O(n) | Usually fastest |
| Space Optimized | O(n) | O(1) | Best space efficiency |

## Pro Tips

1. **Always start with the naive recursive solution** - it helps understand the problem structure
2. **Memoization is often just adding a cache to recursion** - very mechanical transformation
3. **Bottom-up DP is usually preferred in interviews** - shows strong understanding
4. **Look for space optimization opportunities** - demonstrates advanced thinking
5. **Practice identifying the state and transitions** - core skill for DP problems

## Common DP Patterns

- **Linear DP:** Problems with 1D state space (like Fibonacci)
- **Grid DP:** 2D problems (like unique paths)
- **Interval DP:** Problems on ranges or intervals
- **Tree DP:** Dynamic programming on trees
- **Bitmask DP:** Using bit manipulation with DP

Remember: Dynamic Programming is essentially **smart recursion with memory**!
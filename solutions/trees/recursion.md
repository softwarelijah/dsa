# Recursion Notes

## What is Recursion?

Recursion is a programming technique where a function calls itself to solve a problem. It's particularly useful for problems that can be broken down into smaller, similar subproblems.

## Fibonacci Sequence Example

The Fibonacci sequence is a classic example of recursion. The sequence starts with 0 and 1, and each subsequent number is the sum of the previous two numbers.

**Sequence:** 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

### Mathematical Definition

- `F(0) = 0` (base case)
- `F(1) = 1` (base case)
- `F(n) = F(n-1) + F(n-2)` for n > 1 (recursive case)

### Python Implementation

```python
def F(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case
        return F(n-1) + F(n-2)
```

### How F(5) is Computed

```
F(5) = F(4) + F(3)
├── F(4) = F(3) + F(2)
│   ├── F(3) = F(2) + F(1)
│   │   ├── F(2) = F(1) + F(0) = 1 + 0 = 1
│   │   └── F(1) = 1
│   │   └── Result: F(3) = 1 + 1 = 2
│   └── F(2) = F(1) + F(0) = 1 + 0 = 1
│   └── Result: F(4) = 2 + 1 = 3
└── F(3) = 2 (computed same as above)
└── Result: F(5) = 3 + 2 = 5
```

## Recursive Call Stack

When a function calls itself, it creates a **call stack** - a stack data structure that keeps track of function calls.

### Call Stack Components

Each function call on the stack stores:
- **Local variables** (e.g., `n = 4`)
- **Return address** (memory address to return to when function completes)

### Call Stack Example for F(4)

```
Stack grows upward ↑

F(1) [n=1, addr=D] → Base case, returns 1
F(2) [n=2, addr=C] → Needs F(1) + F(0)
F(3) [n=3, addr=B] → Needs F(2) + F(1) 
F(4) [n=4, addr=A] → Needs F(3) + F(2)
```

## Time and Space Complexity

### Fibonacci Recursion Complexity

- **Time Complexity:** `O(2^n)`
    - Each call branches into 2 recursive calls
    - Creates exponential growth
    - Example: F(100) would require ~2^100 operations

- **Space Complexity:** `O(n)`
    - Maximum depth of call stack is n
    - Stack stores n function calls simultaneously

### Why Fibonacci Recursion is Inefficient

The recursive approach recalculates the same values multiple times:
- F(3) is calculated twice when computing F(5)
- F(2) is calculated three times when computing F(5)
- This creates massive redundancy

## Common Recursive Data Structures

### 1. Linked Lists
Linked lists are naturally recursive - each node points to another node (or null).

```
1 → 2 → 3 → 4 → null
```

### 2. Trees
Trees are recursive structures where each node has child nodes.

```
    1
   / \
  2   3
 /   / \
4   5   6
```

### 3. Graphs
Graphs can also be traversed recursively.

## Practical Example: Print Linked List in Reverse

### Problem
Given a linked list `1 → 3 → 4 → 7 → null`, print nodes in reverse order: `7, 4, 3, 1`

### Solution

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_print(node):
    # Base case: reached end of list
    if node is None:
        return
    
    # Recursive call: process next node first
    reverse_print(node.next)
    
    # Print current node after returning from recursion
    print(node.val)

# Example usage:
# head = ListNode(1, ListNode(3, ListNode(4, ListNode(7))))
# reverse_print(head)  # Output: 7, 4, 3, 1
```

### How It Works

1. Start at head (1), don't print yet
2. Recursively call on next node (3)
3. Continue until reaching null (base case)
4. As we return from each call, print the current node
5. This naturally prints in reverse order

### Complexity for Reverse Print
- **Time Complexity:** `O(n)` - visit each node once
- **Space Complexity:** `O(n)` - call stack depth equals list length

## Key Principles of Recursion

1. **Base Case(s):** Condition(s) where recursion stops
2. **Recursive Case:** Function calls itself with modified parameters
3. **Progress:** Each recursive call should move closer to base case
4. **Call Stack:** Each recursive call is stored on the stack

## When to Use Recursion

**Good for:**
- Tree/graph traversal
- Divide and conquer algorithms
- Problems with recursive mathematical definitions
- Backtracking problems

**Consider alternatives when:**
- Simple iterative solution exists
- Stack overflow risk (deep recursion)
- Performance is critical (due to function call overhead)

## Important Notes

- Always ensure base cases are reachable
- Be aware of space complexity due to call stack
- Consider iterative alternatives for better performance
- Use memoization to optimize recursive solutions with overlapping subproblems
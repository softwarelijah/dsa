# Binary Trees - Complete Guide

## What is a Binary Tree?

A **binary tree** is a data structure where each node has at most two children, called the left child and right child.

### Node Structure
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left    # Reference to left child node (or None)
        self.right = right  # Reference to right child node (or None)
```

### Important Terminology

- **Root**: The topmost node in the tree (entry point)
- **Leaf nodes**: Nodes with no children (both left and right are None)
- **Parent**: A node that has children
- **Children**: Nodes directly connected below a parent
- **Subtree**: Any node can be considered the root of its own subtree
- **Height/Maximum Depth**: The longest path from root to any leaf node

### Types of Binary Trees

#### Complete Tree (Full Tree)
- All levels are fully filled except possibly the last level
- Last level is filled from left to right
- Missing nodes only on the right side of the last level

#### Perfect Tree
- All levels are completely filled
- All leaf nodes are at the same level
- Number of nodes at each level: 1, 2, 4, 8, 16... (powers of 2)

### Array Representation

Binary trees can be represented as arrays where:
- Index 1: Root node (index 0 is left blank)
- For node at index `i`:
    - Left child: `2 * i`
    - Right child: `2 * i + 1`
- If index exceeds array length, the child is null

Example: `[_, 1, 2, 3, 4, 5, 10]`

## Tree Traversals

### Depth-First Search (DFS)
Uses a **stack** (or recursion which uses call stack). Prioritizes depth over breadth.

#### Pre-order Traversal
Order: **Node → Left → Right**
```python
def preorder(node):
    if not node:
        return
    print(node.val)      # Process current node
    preorder(node.left)  # Go left
    preorder(node.right) # Go right
```

#### In-order Traversal
Order: **Left → Node → Right**
```python
def inorder(node):
    if not node:
        return
    inorder(node.left)   # Go left
    print(node.val)      # Process current node
    inorder(node.right)  # Go right
```

#### Post-order Traversal
Order: **Left → Right → Node**
```python
def postorder(node):
    if not node:
        return
    postorder(node.left)  # Go left
    postorder(node.right) # Go right
    print(node.val)       # Process current node
```

#### Iterative DFS (Pre-order)
```python
def preorder_iterative(node):
    if not node:
        return
    
    stack = [node]
    while stack:
        current = stack.pop()
        print(current.val)
        
        # Add right first, then left (stack is LIFO)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
```

### Breadth-First Search (BFS)
Uses a **queue**. Prioritizes breadth over depth (level-by-level traversal).

#### Level Order Traversal
```python
from collections import deque

def level_order(node):
    if not node:
        return
    
    queue = deque([node])
    while queue:
        current = queue.popleft()
        print(current.val)
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
```

### Time and Space Complexity
- **Time**: O(n) for all traversals (must visit every node)
- **Space**: O(n) in worst case
    - DFS: O(h) where h is height, but h can be n in worst case (skewed tree)
    - BFS: O(w) where w is maximum width, can be n/2 ≈ O(n) at last level

## Searching in Binary Trees

### General Binary Tree Search
```python
def search(node, target):
    if not node:
        return False
    
    if node.val == target:
        return True
    
    # Must search both sides
    return search(node.left, target) or search(node.right, target)
```
- **Time**: O(n) - may need to check every node
- **Space**: O(n) - recursive call stack

## Binary Search Trees (BST)

A **Binary Search Tree** maintains the property:
- For every node: all values in left subtree < node value < all values in right subtree

### BST Search (Optimized)
```python
def search_bst(node, target):
    if not node:
        return False
    
    if node.val == target:
        return True
    elif target < node.val:
        return search_bst(node.left, target)  # Go left
    else:
        return search_bst(node.right, target) # Go right
```
- **Time**: O(log n) for balanced tree, O(n) for skewed tree
- **Space**: O(log n) for balanced tree

### BST In-order Traversal
In-order traversal of a BST visits nodes in **sorted order**.

### Height Balance Importance
- **Balanced BST**: Height ≈ log n, search is O(log n)
- **Skewed BST**: Height = n, search becomes O(n) (like a linked list)

## Complete Implementation Example

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.val)

# Create a sample tree
def create_sample_tree():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(10)
    
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    
    return a

# Usage examples
root = create_sample_tree()

# Different traversals will output:
# Pre-order: 1, 2, 4, 5, 3, 10
# In-order: 4, 2, 5, 1, 10, 3
# Post-order: 4, 5, 2, 10, 3, 1
# Level-order: 1, 2, 3, 4, 5, 10
```

## Key Takeaways

1. **DFS vs BFS**: DFS uses stack/recursion, BFS uses queue
2. **BST Advantage**: O(log n) search time when balanced
3. **In-order + BST**: Gives sorted order
4. **Space Complexity**: Always consider recursive call stack depth
5. **Tree Balance**: Critical for BST performance
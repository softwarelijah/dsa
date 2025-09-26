"""
Problem: File System Total Size
-------------------------------
You are given a file system represented as a tree structure.

Each node has:
  - name (string)
  - size (int)
  - children (list of Nodes)

Task:
- Return the total size of all files in the file system (sum of sizes of root and all descendants).

We need to implement this in Python.
"""

class Node:
    def __init__(self, name, size=0):
        self.name = name
        self.size = size
        self.children = []

def total_size(root):
    if not root.children:  # Leaf node
        return root.size
    
    cur_size = root.size  # Include current node’s size too
    for child in root.children:
        cur_size += total_size(child)
    return cur_size


# Example usage
root = Node("root", 10)
child1 = Node("child1", 20)
child2 = Node("child2", 5)
grandchild = Node("grandchild", 15)

child1.children.append(grandchild)
root.children.extend([child1, child2])

print(total_size(root))  
# Output: 50 (10 + 20 + 15 + 5)

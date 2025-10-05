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
- Return the size of all the children in the tree (2, 5, 6, 7) = 20

"""""

class Node:
    def __init__(self, name, size=0,):
        self.name = name
        self.size = size
        self.children = []


def total_size(self, root):
    if not root.children:
        return root.size

    curr_size = root.size

    for child in root.children:
        curr_size += total_size(child)
    return curr_size

root = Node("root", 10)
child1 = Node("child1", 20)
root.children.append(child1)

print(total_size(root))
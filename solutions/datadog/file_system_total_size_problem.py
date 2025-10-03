# """
# Problem: File System Total Size
# -------------------------------
# You are given a file system represented as a tree structure.
#
# Each node has:
#   - name (string)
#   - size (int)
#   - children (list of Nodes)
#
# Task:
# - Return the total size of all files in the file system (sum of sizes of root and all descendants).
# - Return the size of all the children in the tree (2, 5, 6, 7) = 20
#
# We need to implement this in Python.
# """
#
# class Node:
#     def __init__(self, name, size=0):
#         self.name = name
#         self.size = size
#         self.children = []
#
# def total_size(root):
#     if not root.children:  # Leaf node
#         return root.size
#
#     cur_size = root.size  # Include current node’s size too
#
#     # i is child
#     for i in root.children:
#         cur_size += total_size(i) # recursive call
#     return cur_size
#
#
# # Example usage
# root = Node("root", 10)
# child1 = Node("child1", 20)
# child2 = Node("child2", 5)
# grandchild = Node("grandchild", 15)
#
# child1.children.append(grandchild)
# root.children.extend([child1, child2])
#
# print(total_size(root))
# # Output: 50 (10 + 20 + 15 + 5)



""
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

"""

class Node:
    def __init__(self, name, size=0):
        self.name = name
        self.size = size
        self.children = []


# takes a node and returns the total size of that node and all of its descendants
# the function doesn't just calculate the root size, it calculates the size of the entire substree from that node
def total_size(root):

    # base case, if the node has no children, it's a leaf node, so just return its size
    # this is the stopping condition, the leaf node is the simplest case, it has no children to process
    # we can directly return its size with no calculation
    if not root.children:
        return root.size

    # initialize current size
    # we start here because the total size includes THIS nodes size
    # then we will add all children's sizes to this
    # were building up the total size piece by piece
    cur_size = root.size


    # here we are looping through the children
    # when we use recursion, we are going to trust that it will correctly return total size of child's entire subtree
    for child in root.children:
        # this is simply recursively going down all the nodes and adding their size into the current size
        cur_size += total_size(child)
        # then return all of those values together
    return cur_size

# Usage:
root = Node("root", 10)
child1 = Node("child1", 20)
root.children.append(child1)

print(total_size(root))  # ← Pass the root node





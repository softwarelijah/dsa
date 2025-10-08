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

class Node():
  def __init__(self, name: str, size=0):
    self.name = name
    self.size = size
    self.children = []


def total_size(root):

  if not root.children:
    return root.size
  curr_size = root.size
  for child in root.children:
    curr_size += total_size(child)
  return curr_size


def total_size_test():

  root1 = Node("file.txt", 10)
  result = total_size(root1)
  assert result == 10, "test 1 failed (no children test)"
  print("test 1 passed (no children)")


  root2 = Node("root", 5)
  child1 = Node("c1", 10)
  child2 = Node("c2", 50)
  root2.children = [child1, child2]

  result = total_size(root2)
  assert result == 65, "test 2 failed (2 children + root = 65)"
  print("test 2 passed (2 children + root = 65) ")

total_size_test()

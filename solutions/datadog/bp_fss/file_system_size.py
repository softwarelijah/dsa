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


def total_size(root) -> int:

  if not root.children:
    return root.size
  
  curr_size = root.size
  for child in root.children:
    curr_size += total_size(child)
  return curr_size


def total_size_test():

  # test 1: single node (no children)
  root1 = Node("file.txt", 10)
  result = total_size(root1)
  assert result == 10, "Test 1 failed"
  print("test 1 passed: single node")

  # test 2: simple tree
  root2 = Node("root", 2)
  child1 = Node("child1", 5)
  child2 = Node("child2", 6)
  root2.children = [child1, child2]

  result = total_size(root2)
  assert result == 13, "Test 2 failed"
  print("Test 2 passed: simple tree")

  # test 3: input given in question
  root3 = Node("root", 2)
  c1 = Node("c1", 5)
  c2 = Node("c2", 6)
  c3 = Node("c3", 7)
  root3.children = [c1, c2, c3]

  result = total_size(root3)
  assert result == 20, "Test 3 failed"
  print("Test 3 passed: multi-level tree (2+5+6+7=20)")

total_size_test()



  







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

"""
TIME COMPLEXITY: O(n)
- Where n is the total number of nodes in the file system tree
- Each node is visited exactly once during the recursive traversal
- At each node, we perform constant-time operations (addition) plus recursive calls to children
- Even though we iterate through children at each node, the total number of iterations
  across all recursive calls equals n (since each node is processed once)
- Total: O(n)

SPACE COMPLEXITY: O(h)
- Where h is the height/depth of the tree
- Space is used by the recursion call stack
- In the worst case (completely unbalanced tree, like a linked list), h = n, so space is O(n)
- In the best case (perfectly balanced tree), h = log(n), so space is O(log n)
- The curr_size variable at each level uses O(1) space
- Total: O(h) where h is the height of the tree

Alternative iterative solution would use O(n) space for an explicit stack/queue but O(1) call stack.

Algorithm Explanation:
- This uses a post-order DFS traversal (process children before using their results)
- Base case: if a node has no children, return its own size
- Recursive case: sum the current node's size with the total sizes of all its children
- Each recursive call returns the total size of the subtree rooted at that node
- This naturally accumulates sizes from leaves up to the root
"""
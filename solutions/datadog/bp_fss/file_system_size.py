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
DATA STRUCTURES:
- N-ary Tree (General Tree): Node class represents a tree structure where each node can have multiple children
  - Each node contains: name (string), size (integer), children (list of Node references)
  - Unlike binary trees, nodes can have any number of children (0 to many)
  - Tree structure represents hierarchical file system organization (directories and files)
- List: children attribute stores references to child nodes
  - Allows iteration over all children of a node
  - Dynamic size accommodates varying numbers of children per node
- Recursion Call Stack: Implicitly maintains the traversal path from root to current node

ALGORITHMS:
- Depth-First Search (DFS): Post-order traversal to explore all nodes in the tree
  - Visits all children before processing the current node
  - Ensures child subtree sizes are computed before parent needs them
  - Base case: leaf nodes (no children) return their own size
  - Recursive case: accumulate sizes from all children plus current node
- Recursion: Function calls itself on each child node to traverse the entire tree
  - Each call processes one subtree and returns its total size
  - Results bubble up from leaves to root
- Accumulation Pattern: Aggregate values from multiple children
  - Initialize with current node's size
  - Iterate through children list, adding each child's subtree size
  - Returns cumulative total for the entire subtree
- Bottom-Up Computation: Calculate results from leaves upward to root
  - Leaf nodes return base values (their own size)
  - Parent nodes combine children's results with their own value
  - Root receives the final accumulated total

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
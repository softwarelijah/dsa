from typing import Optional

"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. 
A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.

Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
"""""

class TreeNode():
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def maxPathSum(root: Optional[TreeNode]) -> int:

  res = [root.val]

  def dfs(root):
    if not root:
      return 0
    
    leftMax = dfs(root.left)
    rightMax = dfs(root.right)

    leftMax = max(leftMax, 0)
    rightMax = max(rightMax, 0)

    res[0] = max(res[0], root.val + leftMax + rightMax)

    return root.val + max(leftMax, rightMax)
  
  dfs(root)
  return res[0]




def maxPathSumTest():

  root1 = TreeNode(10)
  result = maxPathSum(root1)
  assert result == 10, "test 1 failed"
  print("test 1 passed")




  #  [-10,9,20,null,null,15,7]
  root2 = TreeNode(-10)
  root2.left = TreeNode(-9)
  root2.right = TreeNode(20)
  root2.right.left = TreeNode(15)
  root2.right.right = TreeNode(7)

  result = maxPathSum(root2)
  assert result == 42, "test 2 input failed"
  print("test 2 input passed")

maxPathSumTest()

"""
DATA STRUCTURES:
- Binary Tree: TreeNode class represents nodes with val, left, and right pointers
  - Each node contains an integer value and references to left and right children
  - Tree structure allows hierarchical path exploration
- Array (List): res = [root.val] stores the global maximum path sum
  - Single-element list used as a mutable container to share state between nested function scope
  - Allows the inner dfs function to update the global maximum without using nonlocal keyword
- Recursion Call Stack: Implicitly stores the current path from root to current node during DFS

ALGORITHMS:
- Depth-First Search (DFS): Post-order traversal to explore all paths in the tree
  - Visits left subtree, then right subtree, then processes current node
  - Base case: null nodes return 0 (no contribution to path sum)
  - Recursive case: compute max path sums from both subtrees
- Divide and Conquer: Break problem into subproblems for left and right subtrees
  - Combine results from subtrees with current node to find optimal path
- Greedy Selection: At each node, ignore negative path contributions
  - Uses max(leftMax, 0) and max(rightMax, 0) to discard negative sums
  - A negative path would decrease total sum, so it's better to exclude it
- Dynamic Programming (Implicit): Each node's computation depends on optimal solutions from its children
  - Memoization isn't needed because tree structure ensures no repeated subproblems
- Path Sum Calculation: Two key values computed at each node:
  1. Path through node: root.val + leftMax + rightMax (can use both children - inverted V shape)
  2. Path to parent: root.val + max(leftMax, rightMax) (can only extend one branch upward)
- Global Maximum Tracking: Update res[0] with maximum path sum found at any node
  - Ensures we capture the best path even if it doesn't pass through root

TIME COMPLEXITY: O(n)
- Where n is the number of nodes in the binary tree
- The DFS function visits each node exactly once
- At each node, we perform constant-time operations:
  - Two recursive calls (which visit children)
  - Comparison and arithmetic operations: O(1)
- Total: O(n) since we touch every node once

SPACE COMPLEXITY: O(h)
- Where h is the height of the binary tree
- Space is used by the recursion call stack
- In the worst case (skewed tree), h = n, so space is O(n)
- In the best case (balanced tree), h = log(n), so space is O(log n)
- Average case for a balanced tree: O(log n)
- The res array uses O(1) space (single element)
- Total: O(h) where h is the height of the tree

Algorithm Explanation:
- This uses post-order DFS traversal (visit children before processing current node)
- For each node, we calculate two things:
  1. The maximum path sum that PASSES THROUGH this node (root.val + leftMax + rightMax)
     - This can use both left and right subtrees, forming an inverted V shape
  2. The maximum path sum we can RETURN to the parent (root.val + max(leftMax, rightMax))
     - This can only go down one side, as a path can't split at a node and continue upward
- We use max(leftMax, 0) and max(rightMax, 0) to ignore negative paths (better to not include them)
- The res[0] variable tracks the global maximum path sum found at any node
- Using a list [root.val] allows us to mutate the value inside the nested function (closure workaround)
"""
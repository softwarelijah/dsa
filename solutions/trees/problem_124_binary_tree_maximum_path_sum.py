from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:


        # res is a single-item list so dfs() can update the overall max (lists are mutable).
        # Start it with the root's value (there is at least that path).
        res = [root.val]

        # dfs returns the best downward path sum starting at this node (no splitting).
        def dfs(root):
            # No node -> contributes 0.
            if not root:
                return 0

            # Get best downward sums from left and right children.
            left_max = dfs(root.left)
            right_max = dfs(root.right)

            # Ignore negative paths (they would reduce the total).
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            # Path that uses this node as a "split": left + node + right.
            res[0] = max(res[0], root.val + left_max + right_max)

            # Return best single side path to parent: node + max(left, right).
            return root.val + max(left_max, right_max)

        # Start recursion.
        dfs(root)

        # res[0] now has the max path sum anywhere in the tree.
        return res[0]







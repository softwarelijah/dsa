"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. 
A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.
"""""

class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution():

    def maxPathSum(self, root: TreeNode) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            leftMax = dfs(root.right)
            rightMax = dfs(root.left)

            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            res[0] = max(res[0], root.val + leftMax + rightMax)

            return root.val + max(rightMax, leftMax)

        dfs(root)
        return res[0]

root5 = TreeNode(5)
root5.left = TreeNode(4)
root5.right = TreeNode(8)
root5.left.left = TreeNode(11)
root5.left.left.left = TreeNode(7)
root5.left.left.right = TreeNode(2)
root5.right.left = TreeNode(13)
root5.right.right = TreeNode(4)
root5.right.right.right = TreeNode(1)

sol = Solution()
print(sol.maxPathSum(root5))  # Expected: 48 (path: 4->11->7 + 5 + 8 + 13)





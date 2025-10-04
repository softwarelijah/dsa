from typing import Optional

"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. 
A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.
"""

# NOTES:
# we need to find the maximum path sum, in a binary tree where:
# - can start and end at any nodes
# - must follow parent and child connections (can't jump between unrelated notes)
# - each node can only be used once in path

# High Level Strategy
# - using post-order DFS (left, right, then process current node) because we need information from children before
# deciding what to do with the parent


class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:


        # we use a list here because in py integers are immutable, using a list is a common trick because
        # itself is mutable so we can modify res[0] from within the nested function
        # we initialize root.val because that is the minimum possible answer
        res = [root.val]



        def dfs(root):

            # Base Case: if we've reached a null node, it contributes 0 to any path sum.
            # an empty subtree adds nothing
            if not root:
                return 0

            # first recursive calls
            # we first explore the left subtree, then the right subtree (post order pattern)
            # each call returns the maximum path sum we can get starting from that child node and going downward
            # this is crucial, were asking what's the best single direction path I can build from my left child (and right)
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)


            # critical: if a subtree has a negative path sum, were better off NOT including it at all
            # example: if the left subtrees best path is -10, we'd rather take 0 (ignore it) than include it and lost 10 from our total
            # this is why we clamp negative values to 0, we have the option to not go down that path
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # this is where we check the "split" path
            # this path goes from (Up the left subtree, to the current node, and down into the right subtree)
            # root.val + leftMax + rightMax represents
            # current nodes value + best path coming UP from the left (if positive) and plus the best path going DOWN the right (if positive)
            # we compare this against our current best res[0] and keep the maximum
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # what we return to the parent
            # we can only return a single-direction path because the parent might want to extend this path upward
            # we return the current nodes value + plus the better value of the two children (left or right)
            return root.val + max(leftMax, rightMax)

        # start the recursion at the root then return the global maximum we found
        dfs(root)
        return res[0]












# TEST
solution = Solution()

# Test 1: [1,2,3] -> 6
root1 = TreeNode(1, TreeNode(2), TreeNode(3))
print(solution.maxPathSum(root1))

# Test 2: [-10,9,20,null,null,15,7] -> 42
root2 = TreeNode(-10)
root2.left = TreeNode(9)
root2.right = TreeNode(20, TreeNode(15), TreeNode(7))
print(solution.maxPathSum(root2))

# Test 3: Single node [-3] -> -3
root3 = TreeNode(-3)
print(solution.maxPathSum(root3))

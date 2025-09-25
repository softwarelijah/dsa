# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # helper function to check if the tree is valid within given bounds
        def valid(node, left, right):
            # Base case: if we reach a None node, it's valid by default
            if not node:
                return True

            # The current node's value must be strictly between left and right
            if not (node.val < right and node.val > left):
                return False

            # Recursively check the left and right subtrees:
            # - left subtree must be < current node's value
            # - right subtree must be > current node's value
            return (
                valid(node.left, left, node.val) and 
                valid(node.right, node.val, right)
            )
        # Start with the full range of possible values (-∞ to +∞)
        return valid(root, float("-inf"), float("inf"))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # If subRoot is None (empty tree), then it is always a subtree
        if not subRoot:
            return True

        # If root is None but subRoot is not, then subRoot can't be a subtree
        if not root:
            return False
        
        # If the current trees rooted at root and subRoot are the same, return True
        if self.sameTree(root, subRoot):
            return True
        
        # Otherwise, recursively check:
        # - is subRoot a subtree of root's left child? OR
        # - is subRoot a subtree of root's right child?
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

        
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If both nodes are None, trees match up to this point
        if not root and not subRoot:
            return True
        # If both exist and values match, keep checking their children
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right))
        # Otherwise, they don't match
        return False

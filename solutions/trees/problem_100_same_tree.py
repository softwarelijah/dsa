# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # 3x base case
        
        if not p and not q:
            return True # both empties trees
        
        if not p or not q:
            return False # one is null and one is not

        if p.val != q.val:
            return False # if the values are not the same, trees are not the same
        
        # self.isSameTree(p.left, q.left)
        # self.isSameTree(p.left, q.left)

        return (self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left))




        
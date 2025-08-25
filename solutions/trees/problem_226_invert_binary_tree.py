# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # Base case: if the current node is None, there's nothing to invert
        if not root:
            return None
        
        # Recursively invert the right subtree
        right = self.invertTree(root.right)
        
        # Recursively invert the left subtree
        left = self.invertTree(root.left)
        
        # Swap the left and right children of the current node
        root.left = right
        root.right = left
        
        # Return the current node (with its subtrees inverted)
        return root



# Time Complexity: O(n)
  #  - Each node is visited exactly once, where n is the number of nodes in the binary tree.

# Space Complexity: O(h)
  #  - Due to the recursion stack, where h is the height of the tree.
  # - Worst case (unbalanced tree): O(n).
  # - Best case (balanced tree): O(log n).

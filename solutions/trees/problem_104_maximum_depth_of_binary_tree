# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # Base case: if the node is None, its depth is 0
        if root is None:
            return 0
        else:
            # Recursively compute the depth of the left subtree
            left = self.maxDepth(root.left)
            
            # Recursively compute the depth of the right subtree
            right = self.maxDepth(root.right)
            
            # The depth of the current tree is the greater of the two subtrees
            # plus one for the current root node
            return max(left, right) + 1



# Time Complexity: O(n)
  #  - Each node is visited exactly once, where n is the total number of nodes in the tree.

# Space Complexity: O(h)
  #  - h is the height of the tree, representing the maximum depth of the recursion stack.
  # - Best case (balanced tree): O(log n).
  # - Worst case (completely unbalanced tree): O(n).


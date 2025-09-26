# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0             # counter to track how many nodes we've seen so far
        stack = []        # stack to help us simulate recursion (iterative inorder traversal)
        cur = root        # start with the root node

        # Continue as long as there's something to process
        while cur or stack:
            # Go as far left as possible (since left side contains smaller values in a BST)
            while cur:
                stack.append(cur)   # save current node so we can come back later
                cur = cur.left      # move left

            # Once we can't go left anymore, pop the most recent node
            cur = stack.pop()
            n += 1                  # we've "visited" one more node

            # If this is the k-th node we've seen, that's our answer
            if n == k:
                return cur.val

            # Move to the right subtree and repeat the process
            cur = cur.right

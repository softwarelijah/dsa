import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []  # this will hold the final list of levels

        # use a queue to keep track of nodes we need to process
        q = collections.deque()
        q.append(root)  # start by adding the root node

        # keep looping until there are no more nodes in the queue
        while q:
            qLen = len(q)   # number of nodes at the current level
            level = []      # temporary list to store values for this level

            # process all nodes for the current level
            for i in range(qLen):
                node = q.popleft()  # take the next node from the queue
                if node:            # if it's a real node (not None)
                    level.append(node.val)   # add its value to this level
                    q.append(node.left)      # add its left child (even if None)
                    q.append(node.right)     # add its right child (even if None)

            # after finishing one level, if we collected any values, add them to result
            if level:
                res.append(level)

        # return the list of all levels
        return res

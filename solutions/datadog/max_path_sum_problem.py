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


# class TreeNode():
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def maxPathSum(self, root: Optional[TreeNode]) -> int:


#         # we use a list here because in py integers are immutable, using a list is a common trick because
#         # itself is mutable so we can modify res[0] from within the nested function
#         # we initialize root.val because that is the minimum possible answer
#         res = [root.val]



#         def dfs(root):

#             # Base Case: if we've reached a null node, it contributes 0 to any path sum.
#             # an empty subtree adds nothing
#             if not root:
#                 return 0

#             # first recursive calls
#             # we first explore the left subtree, then the right subtree (post order pattern)
#             # each call returns the maximum path sum we can get starting from that child node and going downward
#             # this is crucial, were asking what's the best single direction path I can build from my left child (and right)
#             leftMax = dfs(root.left)
#             rightMax = dfs(root.right)


#             # critical: if a subtree has a negative path sum, were better off NOT including it at all
#             # example: if the left subtrees best path is -10, we'd rather take 0 (ignore it) than include it and lost 10 from our total
#             # this is why we clamp negative values to 0, we have the option to not go down that path
#             leftMax = max(leftMax, 0)
#             rightMax = max(rightMax, 0)

#             # this is where we check the "split" path
#             # this path goes from (Up the left subtree, to the current node, and down into the right subtree)
#             # root.val + leftMax + rightMax represents
#             # current nodes value + best path coming UP from the left (if positive) and plus the best path going DOWN the right (if positive)
#             # we compare this against our current best res[0] and keep the maximum
#             res[0] = max(res[0], root.val + leftMax + rightMax)

#             # what we return to the parent
#             # we can only return a single-direction path because the parent might want to extend this path upward
#             # we return the current nodes value + plus the better value of the two children (left or right)
#             return root.val + max(leftMax, rightMax)

#         # start the recursion at the root then return the global maximum we found
#         dfs(root)
#         return res[0]












# # TEST
# solution = Solution()

# # Test 1: [1,2,3] -> 6
# root1 = TreeNode(1, TreeNode(2), TreeNode(3))
# print(solution.maxPathSum(root1))

# # Test 2: [-10,9,20,null,null,15,7] -> 42
# root2 = TreeNode(-10)
# root2.left = TreeNode(9)
# root2.right = TreeNode(20, TreeNode(15), TreeNode(7))
# print(solution.maxPathSum(root2))

# # Test 3: Single node [-3] -> -3
# root3 = TreeNode(-3)
# print(solution.maxPathSum(root3))





"""
NEW MAX PATH SUM QUESTION, N-ARY TREE INSTEAD
Maximum Path Sum in an N-ary Tree

Problem Statement
Given an N-ary tree where each node contains an integer value and can have any number of children (0 or more), find the maximum path sum in the tree.

A path is defined as any sequence of nodes in the tree where each pair of adjacent nodes has a direct parent-child relationship.  
The path must contain at least one node and does not need to pass through the root.

The path sum is the sum of all node values in the path.

The root of an N-ary tree represented by a Node class with the following structure:

class Node:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

# Clarifications before starting the problem:
# A path is a sequence of nodes where every consecutive pair is a direct parent-child
    # this means you can move up from a child to its parent and down to another child as long as the sequence is continous and doesnt jump

# the path can start and end anywhere (does not need to include the root)
# must be at least one node
# must be a simple path (no cycles or revisiting nodes)
# GOAL: maximum sum over all of the valid paths

# Key observation: at any single node, the best "through this node" path can at most take:
    # one downward branch from one child
    # optionally another downward branch from a different child (path goes from child1 -> node -> child2)
# you can't take 3 or more children at the sanem node, because that would fork that path (not allowed) so at each node, only the top two child contributions matter



# BIG PICTURE OF THE ALGO:

# We do a DFS, for each node we compute:
    # the best sum of a path that starts at this node and goes down into exactly one subtree
    # through-node best to possibly update the global answer

# We keep a global maximum across all nodes

# why initialize the global max to the root's value? 
# if all values are negative, the best path is the single node with the largest (least negative) value:
# initializing with some node value ensures we dont defaukt to 0, (which would be illegal since the path must include one node)


class Node:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children if children is not None else []



# since we are starting at the root, we can only go down one branch. there is no backtracking allowed in paths
# we will be completing this problem bottom up using DFS 

class Solution():
    def maxPathSum(self, root: Node) -> int:
        if not root:
            return 0


        def dfs(node: Node) -> int:
            if not node:
                return 0

            # best child will be used a single cumulative number that represents the best total path sum
            best_child = 0 

            # in this snippet we dont work with the root
            # this is all on the children
            for child in node.children:
                child_down = dfs(child)

                # this line is removing all negatives, since we are trying to find the maximum, no negatives will be counted for
                # "if the best path sum going down from this child is negative, ignore it and treat it as 0"
                child_down = max(child_down, 0)

                # keeps track of the single best child so far
                # so once the loop ends, best child contains the maximum contribution from all children
                # we then return node.val + best_child which is the nodes best root starting path
                best_child = max(child_down, best_child)


            return node.val + best_child # root + best child, here is when we finally work with the root

        # this is where our building comes together into the final answer 
        # "start the recursion at the root node, and calculate the maximum downward path sum starting from the root"
        # or you can think of it as
        # "run a chain reaction of recursive calls throughout the entire tree, gather all the best downward paths and return the single largest total from the root"
        return max(dfs(root), 0)


def test_max_path_sum():

    # this tree looks like
    #     1
    #    /|\
    #   2 3 4
    # so 1 + 4 is the maximum path sum of this tree
    sol = Solution()
    root1 = Node(1, [Node(2), Node(3), Node(4)])
    result = sol.maxPathSum(root1)
    assert result == 5, "test 1 failed"
    print(result, "test 1 passed")

#       5
#      /|\
#    -2 3 -1
    root2 = Node(5, [Node(-2), Node(3), Node(-1)])
    result2 = sol.maxPathSum(root2)
    assert result2 == 8, "test 2 failed"
    print(result2, "test 2 passed")

#       1
#      / \
#     2   3
#    /|
#   4 5
    root3 = Node(1, [Node(2, [Node(4), Node(5)]), Node(3)])
    result3 = sol.maxPathSum(root3)
    assert result3 == 8, "test 3 failed"
    print(result3, "test 3 passed")

    #   10
    #    |
    #   -5
    #    |
    #    20    
    root4 = Node(10, [Node(-5, [Node(20)])])
    result4 = sol.maxPathSum(root4)
    assert result4 == 25, "test 4 failed"
    print(result4, "test 4 passed")

test_max_path_sum()
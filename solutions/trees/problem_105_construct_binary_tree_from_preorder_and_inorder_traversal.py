from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # honestly don't know what is going on with this problem


        # If either list is empty, there is no tree (base case of the recursion).
        if not preorder or not inorder:
            return None

        # The first value in preorder is always the root of the (sub)tree we are building.
        root_val = preorder[0]

        # Make a node for the root value.
        root = TreeNode(root_val)

        # Find where this root value sits inside the inorder list.
        # Everything left of it in inorder belongs to the left subtree,
        # everything right of it belongs to the right subtree.
        mid = inorder.index(root_val)

        # Recursively build the left subtree:
        # preorder[1: mid+1] are the next mid values after the root (they correspond to the left subtree),
        # inorder[:mid] are all the values left of the root in inorder (the left subtree's inorder sequence).
        root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])

        # Recursively build the right subtree:
        # preorder[mid+1:] skips root + left subtree part,
        # inorder[mid+1:] are the values to the right of the root in inorder (the right subtree's inorder sequence).
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        # Return the root of this (sub)tree to be attached by its caller.
        return root




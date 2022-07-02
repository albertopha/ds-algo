# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Complete tree -> # of nodes (2^h - 1)
Hints:
- Getting height is simply iterating left child since complete tree is filled from left to right
- Each recursion is to calculate the number of nodes of subtrees
- Think about the cases when:
  1. left and right heights are equal => left subtree is complete (no dangling leaf node)
  2. left and right heights are NOT equal => right subtree has dangling leaf node
"""
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        
        return pow(2, left_height) + self.countNodes(root.right)\
            if left_height == right_height\
            else pow(2, right_height) + self.countNodes(root.left)
    
    def getHeight(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        return 1 + self.getHeight(node.left)

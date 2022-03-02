# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        inverted = TreeNode(root.val)
        self.invert(root, inverted)
        return inverted
    
    def invert(self, root: Optional[TreeNode], inverted: Optional[TreeNode]) -> None:
        if not root:
            return
        
        inverted.right = TreeNode(root.left.val) if root.left else None
        inverted.left = TreeNode(root.right.val) if root.right else None
        self.invert(root.left, inverted.right)
        self.invert(root.right, inverted.left)
        

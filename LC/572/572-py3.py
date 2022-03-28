# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return not root and not subRoot
        
        if self.validate(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def validate(self, node: Optional[TreeNode], subRootNode: Optional[TreeNode]) -> bool:
        if not node or not subRootNode:
            return not node and not subRootNode
        
        if node.val != subRootNode.val:
            return False
        
        return self.validate(node.left, subRootNode.left) and\
            self.validate(node.right, subRootNode.right) 

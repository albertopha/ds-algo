# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        
        return self.inorderTraverse(root, k)
        
    def inorderTraverse(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        stack = [root]
        node = root
        
        while stack:
            while node and node.left:
                node = node.left
                stack.append(node)
            node = stack.pop()
            count += 1
            if count == k:
                return node.val
            
            node = node.right
            if node:
                stack.append(node)
            
        return -1
    

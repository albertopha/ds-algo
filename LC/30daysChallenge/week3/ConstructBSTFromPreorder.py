# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
      if len(preorder) == 0:
        return
      
      root = TreeNode(preorder[0])
      self.findChildren(root, preorder, 1, len(preorder)-1)
      return root
      
    def findChildren(self, root: TreeNode, preorder: List[int], start: int, end: int) -> None:
      if start > end or not root:
        return
      
      root_val = root.val
      new_start = start
      new_end = end+1
      
      for i in range(start, end+1):
        if root_val > preorder[i]:
            root.left = TreeNode(preorder[i])
            new_start = i
            break
            
      for i in range(start, end+1):
        if root_val < preorder[i]:
            root.right = TreeNode(preorder[i])
            new_end = i
            break
      
      if root.left:
        self.findChildren(root.left, preorder, new_start+1, new_end-1)
        
      if root.right:
        self.findChildren(root.right, preorder, new_end+1, end)
"""
[3,9,20,15,7]
     ^

[3,15,20,7]
      ^

                    3
              /            \
          9                  20
                        /         \
                     [3,15]       [7]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return
        
        node = TreeNode(preorder.pop(0))
        inorder_index = inorder.index(node.val)
        node.left = self.buildTree(preorder, inorder[0: inorder_index])
        node.right = self.buildTree(preorder, inorder[inorder_index+1:])
        return node
    

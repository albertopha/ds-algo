# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q:
            return root
        
        if p == q:
            return p
        
        p_paths = set()
        self.getPaths(root, p, p_paths)
        result = [None]
        self.dfs(root, q, p_paths, result)
        return result[0]
    
    def dfs(self, node: 'TreeNode', target: 'TreeNode', paths: set['TreeNode'], ancestor: List['TreeNode']) -> bool:
        if not node:
            return False
        
        if node == target:
            if ancestor[0] is None and node in paths:
                ancestor[0] = node
            return True
        
        if self.dfs(node.left, target, paths, ancestor) or\
            self.dfs(node.right, target, paths, ancestor):
            if ancestor[0] is None and node in paths:
                ancestor[0] = node
            return True
        
    def getPaths(self, node: 'TreeNode', target: 'TreeNode', paths: set['TreeNode']) -> bool:
        if not node:
            return False
        
        if node == target:
            paths.add(node)
            return True
        
        if self.getPaths(node.left, target, paths) or\
            self.getPaths(node.right, target, paths):
            paths.add(node)
            return True
        
        return False
        

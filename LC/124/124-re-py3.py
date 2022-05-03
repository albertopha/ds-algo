# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_sums = [-sys.maxsize]
        self.maxPathSumRec(root, max_sums)
        return max_sums[0]
    
    def maxPathSumRec(self, node: Optional[TreeNode], max_sums: List[int]) -> int:
        if not node:
            return 0
        
        left_sum = max(self.maxPathSumRec(node.left, max_sums), 0)
        right_sum = max(self.maxPathSumRec(node.right, max_sums), 0)
        
        max_sums[0] = max(max_sums[0], left_sum+right_sum+node.val)
        return max(left_sum+node.val, right_sum+node.val)

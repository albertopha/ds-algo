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
        
        maxSum = [root.val]
        self.maxPathSumRec(root, maxSum)
        return maxSum[0]
        
    def maxPathSumRec(self, node: Optional[TreeNode], maxSum: List[int]) -> int:
        if not node:
            return 0
        
        # Maximum sum from left subtree
        leftSubtreeSum = max(self.maxPathSumRec(node.left, maxSum), 0)
        
        # Maximum sum from right subtree
        rightSubtreeSum = max(self.maxPathSumRec(node.right, maxSum), 0)
        
        # Update the maximum sum
        maxSum[0] = max(maxSum[0], node.val+leftSubtreeSum+rightSubtreeSum)
        
        # Path needs to be connected, meaning we need to either choose left or right subtree
        # and add current node value
        return node.val + max(leftSubtreeSum, rightSubtreeSum)

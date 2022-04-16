# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
from collections import defaultdict

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        m = defaultdict(list)
        self.traversal(root, 0, 0, m)
        
        sorted_cols = sorted(m.keys())
        output = []
        for col in sorted_cols:
            tmp = []
            while m[col]:
                tmp.append(heapq.heappop(m[col])[1])
            output.append(tmp)
        return output
    
    def traversal(self, node: Optional[TreeNode], row: int, col: int, m: dict) -> None:
        if not node:
            return
        
        heapq.heappush(m[col], (row, node.val))
        self.traversal(node.left, row+1, col-1, m)
        self.traversal(node.right, row+1, col+1, m)
   

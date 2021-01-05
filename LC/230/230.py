# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
=======================================================
Test cases:
#1
[3,1,4,null,2]
k = 1

in-order traversal for bst:
1 -> 2 -> 3 -> 4
output: 1
=======================================================
Brute force:
1. In-order traversal into the list.
2. return kth value

Time: O(N) N = # of nodes
Space: O(N) recursion stack
=======================================================
Optimal (slight improvement for smaller datasets):
1. While in-order traversal, return kth value right away.

Time: O(N)
Space: O(N)
======================================================
"""
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if k == 0:
            return root.val
        
        return self.iterative(root, k)
    
    def iterative(self, root, k):
        stack = [root]
        tmp = root
        count = 0
        in_order = []
        
        while stack:
            while tmp and tmp.left:
                stack.append(tmp.left)
                tmp = tmp.left
            
            tmp = stack.pop()
            in_order.append(tmp.val)
            count += 1
            if k == count:
                return tmp.val
            
            tmp = tmp.right
            if tmp:
                stack.append(tmp)
        
        return -1


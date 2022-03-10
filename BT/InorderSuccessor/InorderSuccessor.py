# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, t):
        node = root
        stack = []

        while node or stack:
            while node: 
               stack.append(node)
               node = node.left

            node = stack.pop()
            if node.val > t:
                return node.val;
            node = node.right
        return -1;

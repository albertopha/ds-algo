# ! - J
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) != len(postorder):
            return None

        if len(inorder) == 0:
            if len(postorder) == 0:
              return None
            elif inorder[0] == postorder[0]:
                return TreeNode(inorder[0])
            else:
                return None

        # root_pointer = len(postorder)-1
        # root_value = postorder[root_pointer]
        # root = TreeNode(root_value)
        # inorder_ind = inorder.index(root_value)

        # root.left = self.build_brute_force(inorder_map, postorder, 0, inorder_ind-1)
        # root.right = self.build_brute_force(inorder_map, postorder, inorder_ind+1, len(postorder)-1)

        inorder_map = {inorder[i]: i for i in range(len(inorder))}
        return self.build(inorder_map, postorder, 0, len(postorder) - 1)

        return root

    def build_brute_force(self, inorder: List[int], postorder: List[int], start: int, end: int) -> TreeNode:
        if start > end:
            return None

        curr_inorder_in = -1

        for p in reversed(postorder):
            for i in range(start, end+1):
                if inorder[i] == p:
                    curr_inorder_in = i
                    break
            if curr_inorder_in != -1:
                break

        curr_root = TreeNode(inorder[curr_inorder_in])
        curr_root.left = self.build_brute_force(inorder, postorder, start, curr_inorder_in-1)
        curr_root.right = self.build_brute_force(inorder, postorder, curr_inorder_in+1, end)

        return curr_root

    def build(self, inorder_map: object, postorder: List[int], start: int, end: int) -> TreeNode:
        if start > end:
            return None

        value = postorder.pop()
        curr_inorder_in = inorder_map[value]
        curr_root = TreeNode(value)
        curr_root.right = self.build(inorder_map, postorder, curr_inorder_in+1, end)
        curr_root.left = self.build(inorder_map, postorder, start, curr_inorder_in-1)

        return curr_root

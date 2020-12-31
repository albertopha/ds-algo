# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.getInorder(root, root)

    def getInorder(self, leftRoot: TreeNode, rightRoot: TreeNode) -> None:
        if leftRoot and not rightRoot:
            return False

        if not leftRoot and rightRoot:
            return False

        if leftRoot and rightRoot:
            if leftRoot.val != rightRoot.val:
                return False
            return self.getInorder(leftRoot.left, rightRoot.right) and self.getInorder(leftRoot.right, rightRoot.left)

        return True
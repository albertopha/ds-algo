class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ValidateBST(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result = []
        self.isValidateBST_brute(root, result)

        for i in range(1, len(result)):
            if result[i-1] > result[i]:
                return False

        return True

    def isValidateBST_brute(self, root, result):
        if root:
            self.isValidateBST_brute(root.left, result)
            result.append(root.val)
            self.isValidateBST_brute(root.right, result)


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryInOrder(object):
    def in_order_traversal(self, root):
        result = []
        self.in_order_traversal_rec(root, result)
        return result

    def in_order_traversal_rec(self, root, arr):
        if root:
            self.in_order_traversal_rec(root.left, arr)
            if root is not None:
                arr.append(root.val)
            self.in_order_traversal_rec(root.right, arr)

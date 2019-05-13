#!
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class UniqueBinarySearchTree2(object):
    def generate_trees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []

        return self.generate_trees_brute(1, n)

    def generate_trees_brute(self, start, end):
        trees = []

        if start > end:
            trees.append(None)
            return trees

        i = start
        while i <= end:
            left_tree = self.generate_trees_brute(start, i-1)
            right_tree = self.generate_trees_brute(i+1, end)
            for l in left_tree:
                for r in right_tree:
                    curr = TreeNode(i)
                    curr.left = l
                    curr.right = r
                    trees.append(curr)
            i += 1

        return trees

    def print_result(self, arr):
        for root in arr:
            self.print_tree_inorder(root)

    def print_tree_inorder(self, root):
        if root:
            self.print_tree_inorder(root.left)
            print(root.val)
            self.print_tree_inorder(root.right)


if __name__ == '__main__':
    ubst = UniqueBinarySearchTree2()
    generated_tree = ubst.generate_trees(3)
    ubst.print_result(generated_tree)
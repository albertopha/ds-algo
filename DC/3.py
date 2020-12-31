# !
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree(object):
    def serialize(self, root):
        serialized = []
        self.serialize_helper(root, serialized)
        return '-'.join(serialized)

    def serialize_helper(self, root, serialized):
        if root is None:
            return

        serialized.append(root.val)
        self.serialize_helper(root.left, serialized)
        self.serialize_helper(root.right, serialized)

    def deserialize(self, serialized):
        serialized_list = serialized.split('-')

        if len(serialized_list) == 0:
            return

        root = Node('root')

        for i in range(1, len(serialized_list)):
            curr = serialized_list[i].split('.')
            curr_root = root

            for j in range(len(curr)-1):

                if curr[j] == 'left':
                    curr_root = curr_root.left
                else:
                    curr_root = curr_root.right

            last_child = curr[-1]

            if last_child == 'left':
                curr_root.left = Node(serialized_list[i])
            else:
                curr_root.right = Node(serialized_list[i])

        return root

    def print_tree(self, root):
        if root:
            print(root.val)
            self.print_tree(root.left)
            self.print_tree(root.right)


if __name__ == '__main__':
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    tree = Tree()
    serialized = tree.serialize(node)
    deserialized = tree.deserialize(serialized)
    tree.print_tree(deserialized)
    assert tree.deserialize(serialized).left.left.val == 'left.left'
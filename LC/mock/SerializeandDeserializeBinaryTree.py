import math


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""

        queue = [root]
        result = []
        while len(queue) > 0:
            inner_queue = list(queue)
            queue = []
            while len(inner_queue) > 0:
                curr = inner_queue.pop(0)

                if curr is None:
                    result.append("null")
                else:
                    result.append(str(curr.val))
                    queue.append(curr.left)
                    queue.append(curr.right)
        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None

        data_list = data.split(",")

        root = TreeNode(int(data_list[0]))
        queue = [root]
        i = 1

        while len(queue) > 0:
            inner_queue = list(queue)
            queue = []

            while len(inner_queue) > 0:
                curr = inner_queue.pop(0)

                if curr != "null":
                    if i < len(data_list):
                        if data_list[i] != "null":
                            curr.left = TreeNode(int(data_list[i]))
                            queue.append(curr.left)
                        queue.append("null")

                    if i + 1 < len(data_list):
                        if data_list[i + 1] != "null":
                            curr.right = TreeNode(int(data_list[i + 1]))
                            queue.append(curr.right)
                        else:
                            queue.append("null")

                    i += 2

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
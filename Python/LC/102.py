#!
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        queue = [root]

        if root is None:
            return result

        while len(queue) > 0:
            new_queue, inner_queue = [], []
            for curr in queue:
                inner_queue.append(curr.val)

                if curr.left:
                    new_queue.append(curr.left)

                if curr.right:
                    new_queue.append(curr.right)

            result.append(inner_queue)
            queue = new_queue

        return result
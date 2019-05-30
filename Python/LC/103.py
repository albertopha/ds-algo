# !
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        result = []
        direction = 0  # 0 for left; 1 otherwise

        while len(queue):
            children = queue[:]
            queue = []
            aux = []
            while len(children):
                curr = children.pop(0) if direction == 0 else children.pop(len(children) - 1)
                aux.append(curr.val)

                if direction == 0:
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                else:
                    if curr.right:
                        queue.insert(0, curr.right)
                    if curr.left:
                        queue.insert(0, curr.left)

            if direction == 0:
                direction = 1
            else:
                direction = 0
            result.append(aux)

        return result

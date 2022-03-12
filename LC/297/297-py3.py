# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        
        queue = deque([root])
        serialized = []
        
        while queue:
            node = queue.popleft()
            if not node:
                serialized.append('null')
            else:
                serialized.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            
        return ",".join(serialized)
        

    """
    [1,2,3,null,null,4,5,null,null,null,null]
    """
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        
        serialized = deque(data.split(","))
        root = TreeNode(serialized[0])
        serialized.popleft()
        
        queue = deque([root])
        while queue:
            node = queue.popleft()
            left = serialized.popleft()
            right = serialized.popleft()
            
            node.left = TreeNode(int(left)) if left != 'null' else None
            node.right = TreeNode(int(right)) if right != 'null' else None
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""

class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if(node is None):
            return node

        visited, queue = {node: Node(node.val, [])}, collections.deque()
        queue.append(node)

        while(queue):
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if(neighbor not in visited):
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                visited[curr].neighbors.append(visited[neighbor])

        return visited[node]
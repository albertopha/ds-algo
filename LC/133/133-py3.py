"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        
        cloned = Node(node.val)
        look_up = dict()
        self.dfs(node, cloned, look_up)
        return cloned
    
    def dfs(self, node: 'Node', cloned: 'Node', look_up: dict) -> None:
        if not node or node.val in look_up:
            return
        
        look_up[node.val] = cloned
        
        for neighbor in node.neighbors:
            cloned_neighbor = look_up[neighbor.val] if neighbor.val in look_up else Node(neighbor.val)
            cloned.neighbors.append(cloned_neighbor)
            self.dfs(neighbor, cloned_neighbor, look_up)
                
                
        
            

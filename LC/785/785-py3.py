from collections import defaultdict

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph:
            return False
        
        # -1 for uncolored, 0 for red and 1 for blue
        color_map = defaultdict(lambda: -1)
        unvisited_list = [i for i in range(len(graph))]
        unvisited = set(unvisited_list)
        
        while unvisited:
            start_node = unvisited.pop()
            if not self.dfs(graph, start_node, unvisited, color_map):
                return False
                
        return True
    
    def dfs(self, graph: List[List[int]], start_node: int, unvisited: set, color_map: dict) -> bool:
        stack = [start_node]
        color_map[start_node] = 0
        
        while stack:
            node = stack.pop()
            color = color_map[node]
            if node in unvisited:
                unvisited.remove(node)
            
            for next_node in graph[node]:
                if next_node not in unvisited:
                    continue
                
                next_color = color_map[next_node]
                
                if next_color != -1 and next_color == color:
                    return False
                
                color_map[next_node] = 1 if color == 0 else 0
                stack.append(next_node)
        return True
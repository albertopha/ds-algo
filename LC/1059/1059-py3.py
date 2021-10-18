from collections import defaultdict

class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if not edges:
            return source == destination
        
        graph = self.construct(edges)
        return self.dfs(source, destination, graph, [0]*n)
    
    def construct(self, edges: List[List[int]]) -> dict:
        graph = defaultdict(set)
        
        for source, target in edges:
            graph[source].add(target)
        
        return graph
    
    def dfs(self, node: int, destination: int, graph: dict, state: List[int]) -> bool:
        if state[node] != 0:
            return state[node] == 2
        
        if not graph[node]:
            return node == destination
        
        state[node] = 1
        for neighbour in graph[node]:
            if not self.dfs(neighbour, destination, graph, state):
                return False
        
        state[node] = 2
        return True

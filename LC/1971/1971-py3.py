class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        if not edges or start == end:
            return start == end
        
        graph = self.construct(n, edges)
        return self.dfsIterative(start, end, graph)
    
    def construct(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        
        for source, target in edges:
            graph[source].append(target)
            graph[target].append(source)
        
        return graph
    
    def dfsIterative(self, node: int, target: int, graph: dict) -> bool:
        stack = [node]
        seen = set()
        seen.add(node)
        
        while stack:
            n = stack.pop()
                
            for neighbour in graph[n]:
                if neighbour in seen:
                    continue
                if neighbour == target:
                    return True
                seen.add(neighbour)
                stack.append(neighbour)
                
        return False
        
    def dfs(self, node: int, target: int, graph: List[List[int]]) -> bool:
        if node == target:
            return True
        
        for neighbour, connection in enumerate(graph[node]):
            if connection:
                graph[node][neighbour] = 0
                if self.dfs(neighbour, target, graph):
                    return True
        return False
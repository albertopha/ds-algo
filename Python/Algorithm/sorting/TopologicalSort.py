class TopologicalSort(object):
    def __init__(self):
        return

    def topologicalSort(self, vertices, edges):
        """
        :type vertices: int
        :type edges: List[List[int]]
        """
        if not edges or len(edges[0]) == 0:
            return []

        graph = self.generateGraph(edges)
        sorts = [-1 for _ in range(vertices)]
        print('graph -> ', graph)
        first_elem = edges[0][0]
        visited = set()
        index = [vertices - 1]
        for source, target in edges:
            if source not in visited:
                self.dfs(graph, source, index, sorts, visited)

            if target not in visited:
                self.dfs(graph, target, index, sorts, visited)
        return sorts

    def dfs(self, graph, vertex, index, sorts, visited):
        if vertex in graph:
            for v in graph[vertex]:
                if v not in visited:
                    self.dfs(graph, v, index, sorts, visited)

        visited.add(vertex)
        sorts[index[0]] = vertex
        index[0] -= 1
    
    def generateGraph(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: Object
        """
        graph = dict()
        for source, target in edges:
            if source not in graph:
                graph[source] = set()
            graph[source].add(target)

        return graph

    def topologicalSortBFS(self, vertices, edges):
        sorted_order = []
        if vertices <= 0:
            return sorted_order

        # Initialize the graph
        in_degree = {_: 0 for _ in range(vertices)}
        graph = {_: [] for _ in range(vertices)}

        # Create graph
        for source, target in edges:
            graph[source].append(target)
            in_degree[target] += 1

        # Enqueue nodes with zero in degree
        queue = deque()
        for node in in_degree:
            if in_degree[node] == 0:
                queue.append(node)

        while queue:
            vertex = queue.popleft()
            sorted_order.insert(0, vertex)

            for target in graph[vertex]:
                in_degree[target] -= 1
                if in_degree[target] == 0:
                    queue.append(target)

        if len(sorted_order) != vertices:
            return []
        return sorted_order
if __name__ == "__main__":
    ts = TopologicalSort()
    vertices = 5
    edges = [[4, 2],
                [4, 3],
                [2, 0],
                [2, 1],
                [3, 1]]
    print(ts.topologicalSort(vertices, edges))
    
    vertices = 7
    edges = [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]]
        
        
        
        
        
        
    print(ts.topologicalSort(vertices, edges))

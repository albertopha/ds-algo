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

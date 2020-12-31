class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if not prerequisites:
            return [a for a in reversed(range(numCourses))]
        
        return self.topologicalSort(numCourses, prerequisites)
        
    def topologicalSort(self, courses, prereqs):
        sorted_order = []
        if courses <= 0:
            return sorted_order

        # Initialize the graph
        in_degree = {_: 0 for _ in range(courses)}
        graph = {_: [] for _ in range(courses)}

        # Create graph
        for source, target in prereqs:
            graph[source].append(target)
            in_degree[arget] += 1

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

        if len(sorted_order) != courses:
            return []
        return sorted_ordert

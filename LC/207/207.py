#! Re - J
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if len(prerequisites) == 0:
            return True

        graph = self.form_graph(prerequisites)

        if len(graph.keys()) > numCourses:
            return False

        for preq in prerequisites:
            start = preq[0]

            if self.find_cycle(graph, start, {}):
                return False

        return True

    @staticmethod
    def form_graph(vertices: List[List[int]]) -> dict:
        graph = {}

        for vertex in vertices:
            start = vertex[0]
            end = vertex[1]

            if start not in graph:
                graph[start] = [end]
            else:
                graph[start].append(end)

            if end not in graph:
                graph[end] = []

        return graph

    def find_cycle(self, graph: dict, vertex: int, visited: dict) -> bool:
        neighbours = graph[vertex] if vertex in graph else []

        if vertex in visited and visited[vertex]:
            return True

        visited[vertex] = True

        for neighbour in neighbours:
            if self.find_cycle(graph, neighbour, visited):
                return True

        visited[vertex] = False

        return False


if __name__ == '__main__':
    s = Solution()
    print(s.canFinish(2, [[1,0]]))
    print(s.canFinish(2, [[1,0],[0,1]]))
    print(s.canFinish(2, [[1,2],[2,3]]))
    print(s.canFinish(3, [[1,2],[2,3]]))
    print(s.canFinish(3, [[0,1],[0,2],[1,2]]))
    print(s.canFinish(4, [[2,0],[1,0],[3,1],[3,2],[1,3]]))


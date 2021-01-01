"""
Problem Statement:
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, write a method to print all possible ordering of tasks meeting all prerequisites.
"""

from collections import defaultdict

def getAllTaskScheduleOrders(tasks, prereqs):
    if tasks <= 0:
        return []

    in_degree = defaultdict(lambda: 0)
    graph = defaultdict(lambda: set())

    for source, target in prereqs:
        graph[source].add(target)
        in_degree[target] += 1

    queue = []
    for node in range(tasks):
        if in_degree[node] == 0:
            queue.append(node)

    print('tasks -> ', tasks)
    print('start queue -> ', queue)
    output = []
    generateAllSchedules(tasks, graph, in_degree, queue, [], output)
    return output

def generateAllSchedules(tasks, graph, in_degree, queue, current, output):
    if queue:
        for vertex in queue:
            current.append(vertex)
            next_queue = list(filter(lambda x: x != vertex, queue))

            for child in graph[vertex]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    next_queue.append(child)

            generateAllSchedules(tasks, graph, in_degree, next_queue, current, output)

            current.pop()
            for child in graph[vertex]:
                in_degree[child] += 1

    if len(current) == tasks:
        output.append(current[:])

if __name__ == "__main__":
    vertices = 5
    edges = [[4, 2],
            [4, 3],
            [2, 0],
            [2, 1],
            [3, 1]]
    print(getAllTaskScheduleOrders(vertices, edges))

    vertices = 7
    edges = [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]]
    print(getAllTaskScheduleOrders(vertices, edges))

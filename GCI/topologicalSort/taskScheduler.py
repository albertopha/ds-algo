"""
Problem statement:
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, find out if it is possible to schedule all the tasks.
"""
from collections import defaultdict

def taskScheduler(tasks, prerequisites):
    if tasks <= 0:
        return True

    sorts = topologicalSort(tasks, prerequisites)
    print('sorts -> ', sorts)
    if tasks != len(sorts):
        return False
    return True

def topologicalSort(tasks, prereqs):
    # Initialize graph
    graph = defaultdict(lambda: set())

    # Initialize in_degree (number of incoming edges)
    in_degree = defaultdict(lambda: 0)

    for source, target in prereqs:
        graph[source].add(target)
        in_degree[target] += 1

    # Initialize queue with nodes with 0 degree
    # In other words, tasks without prereqs
    queue = []
    for task in range(tasks):
        if in_degree[task] == 0:
            queue.append(task)

    sorts = []
    # BFS
    while queue:
        task = queue.pop(0)
        sorts.append(task)

        for next_task in graph[task]:
            in_degree[next_task] -= 1
            if in_degree[next_task] == 0:
                queue.append(next_task)
    return sorts

# Example 1
tasks, prereqs = 3, [[0, 1], [1, 2]]
print(taskScheduler(tasks, prereqs))

# Example 2
tasks, prereqs = 3, [[0, 1], [1, 2], [2, 0]]
print(taskScheduler(tasks, prereqs))

# Example 3
tasks, prereqs = 6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]]
print(taskScheduler(tasks, prereqs))


from collections import deque

def topological_sort(vertices, edges):
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

    sources = deque()
    for target in in_degree:
        if in_degree[target] == 0:
            sources.append(target)

    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)

        for target in graph[vertex]:
            in_degree[target] -= 1
            if in_degree[target] == 0:
                sources.append(target)

    if len(sorted_order) != vertices:
        return []
    return sorted_order

def main():
    print(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]]))
    print(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]]))
    print(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]]))
    print(topological_sort(8, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1], [7, 0]]))
main()

"""
Algorithm:
    1. From each of unvisited vertices, choose teh vertex with the smallest distance and visit it.
    2. Update the distance for each neighbouring vertex, of the visited vertex, whose current distance is greater than its sum and weight of the edge between them.
    3. Repeat step 1 and 2 till all unvisited vertices are visited.
"""

import sys
def dijkstra():
    vertices = [
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0]
    ]
    edges = [
        [0, 3, 4, 0],
        [0, 0, 0.5, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0]
    ]

    visited = set()

    for i in range(len(vertices)):
        unvisited.add(i)

    distance = [[sys.maxint, None] for _ in range(len(vertices))]
    distance[0][0] = 0
    distance[0][1] = None

    for i in range(len(vertices)):
        # Current vertex
        u = find_min_distance(distance, visited)
        visited.add(u)

        # Update the distance of neighbours
        for v in range(len(vertices)):
            if v != 0 and v not in visited and\
                distance[u][0] + edges[u][v] < distance[v][0]:
                    distance[v][0] = distance[u][0] + edges[u][v]
                    distance[v][1] = u


def find_min_distance(distance, visited):
    min_distance = sys.maxint
    min_vertex = -1

    for i in range len(distance):
        if i not in visited and distance[i][0] < min_distance:
            min_distance = distance[i][0]
            min_vertex = i

    return min_vertex 


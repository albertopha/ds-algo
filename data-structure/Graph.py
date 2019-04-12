class DirectedGraph:
    def __init__(self):
        self.adj = {}

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def add_edges(self, start, end):
        if start in self.adj:
            self.adj[start].append(end)

    def delete_vertex(self, v):
        for value in self.adj:
            if v in value:
                value.remove(v)

            self.adj.pop(v)

    def delete_edge(self, v, end):
        if v in self.adj:
            if end in self.adj[v]:
                self.adj[v].remove(end)


class WeightedDirectedGraph:
    def __init__(self):
        self.adj = {}

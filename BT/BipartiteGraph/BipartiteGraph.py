class Solution:
    def solve(self, graph):
        if not graph:
            return True

        reds, blacks = set(), set()
        for start_node in range(len(graph)):
            if start_node in reds or start_node in blacks:
                continue
            if not self.dfs(graph, start_node, True, blacks, reds):
                return False
        return True

    def dfs(self, graph, node, is_black, blacks, reds):
        if node in blacks or node in reds:
            return (is_black and  node in blacks) or (not is_black and node in reds)
        
        if is_black:
            blacks.add(node)
        else:
            reds.add(node)
        
        for child in graph[node]:
            if not self.dfs(graph, child, not is_black, blacks, reds):
                return False
        
        return True

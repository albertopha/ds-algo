class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph:
            return []
        
        paths = []
        stack = [[0]]
        while stack:
            current_path = stack.pop()
            source = current_path[-1]
            
            for target in graph[source]:
                cloned_path = current_path[:]
                cloned_path.append(target)
                
                if target == len(graph)-1:
                    paths.append(cloned_path)
                    continue
                
                stack.append(cloned_path)
        
        return paths
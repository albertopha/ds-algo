from collections import defaultdict, deque

class TopologicalSort:
    
    def __init__(self):
        pass
    
    def sort(self, size: int, relations: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        incoming_count = defaultdict(int, { k: 0 for k in range(size)})
        output = []
        
        for target, source in relations:
            graph[source].append(target)
            incoming_count[target] += 1
        
        queue = deque()
        for key, value in incoming_count.items():
            if value == 0:
                queue.append(key)
        
        while queue:
            node = queue.pop()
            
            if incoming_count[node] == 0:
                output.append(node)
            
            for neighbour in graph[node]:
                incoming_count[neighbour] -= 1
                if incoming_count[neighbour] == 0:
                    queue.appendleft(neighbour)
        
        # Found cycle
        if len(output) != size:
            return []
    
        return output

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not numCourses:
            return []
        
        ts = TopologicalSort()
        return ts.sort(numCourses, prerequisites)
        
        

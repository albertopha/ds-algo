class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        if not regions:
            return ""
        
        if region1 == region2:
            return region1
        
        graph = self.construct(regions)
        ancestors = self.getAncestors(graph, region1)
        
        if region2 in ancestors:
            return region2
        
        while region2 in graph:
            region2 = graph[region2]
            if region2 in ancestors:
                return region2 
        
        return ""
        
    def getAncestors(self, graph: dict, region: str) -> set:
        ancestors = set()
        ancestors.add(region)
        
        while region in graph:
            region = graph[region]
            ancestors.add(region)
        
        return ancestors
        
    def construct(self, regions: List[List[str]]) -> dict:
        graph = dict()
        
        for region in regions:
            parent = region[0]
            for i in range(1, len(region)):
                child = region[i]
                if child not in graph:
                    graph[child] = ""
                graph[child] = parent
            
        return graph
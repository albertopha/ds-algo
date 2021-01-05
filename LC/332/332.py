"""
["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]

adjacents = {
    "JFK": ["SFO", "ATL"]
    "SFO": ["ATL"]
    "ATL": ["JFK", "SFO"]
}

 {
     'JFK': [u'ANU', u'TIA'],
     'EZE': [u'AXA'],
     'AXA': [u'TIA'],
     'TIA': [u'ANU', u'ANU', u'JFK'],
     'ANU': [u'JFK', u'EZE', u'TIA']
 }
"""
from collections import defaultdict

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        if not tickets:
            return []
        
        adjacents = defaultdict(lambda: [])
        for f, t in tickets:
            adjacents[f].append(t)
        
        visited = dict()
        for origin, itinerary in adjacents.items():
           itinerary.sort()
            visited[origin] = [False]*len(itinerary)
        
        output = ["JFK"]
        self.dfs(adjacents, "JFK", len(tickets), output, visited)
        return output
        
    
    def dfs(self, adjacents, airport, total_tickets, current, visited):
        if total_tickets + 1 == len(current):
            return True
        
        for i, next_airport in enumerate(adjacents[airport]):
            if not visited[airport][i]:
                current.append(next_airport)
                visited[airport][i] = True
                if self.dfs(adjacents, next_airport, total_tickets, current, visited):
                    return True
                current.pop()
                visited[airport][i] = False
        
        return False
         

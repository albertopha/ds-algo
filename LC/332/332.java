/*
JFK: [SFO, ATL],
SFO: [ATL],
ATL: [JFK, SFO]

JFK -> SFO -> ATL -> JFK -> ATL -> SFO
JFK -> ATL -> JFK -> SFO -> ATL -> SFO
JFK -> ATL -> SFO -> ATL -> JFK -> SFO

JFK: [SFO, ATL],
SFO: [ATL],
ATL: [JFK]

JFK -> SFO -> ATL -> JFK -> ATL
JFK -> ATL -> JFK -> SFO -> ATL

JFK: [SFO, ATL],
SFO: [],
ATL: [JFK, SFO]
*/
class Solution {
    public List<String> findItinerary(List<List<String>> tickets) {
        if (tickets.size() == 0) return new ArrayList<>();

        List<String> itinerary = new ArrayList<>();
        itinerary.add("JFK");
        Map<String, List<String>> graph = buildGraph(tickets);

        int size = 0;
        Map<String, boolean[]> visitedMap = new HashMap<>();
        for (String from: graph.keySet()) {
            size += graph.get(from).size();
            Collections.sort(graph.get(from));
            visitedMap.put(from, new boolean[graph.get(from).size()]);
        }
        getItinerary("JFK", graph, visitedMap, itinerary, size);
        return itinerary;
    }

    private boolean getItinerary(String from, Map<String, List<String>> graph, Map<String, boolean[]> visitedMap, List<String> itinerary, int size) {
        if (size == 0) return true;

        List<String> tos = graph.getOrDefault(from, new LinkedList<String>());
        boolean[] visited = visitedMap.get(from);

        for (int i = 0; i < tos.size(); i++) {
            if (visited[i]) continue;
            visited[i] = true;
            itinerary.add(tos.get(i));
            if (getItinerary(tos.get(i), graph, visitedMap, itinerary, size-1)) {
                return true;
            }
            itinerary.remove(itinerary.size()-1);
            visited[i] = false;
        }

        return false;
    }

    private Map<String, List<String>> buildGraph(List<List<String>> tickets) {
        Map<String, List<String>> graph = new HashMap<>();
        for (List<String> ticket: tickets) {
            String from = ticket.get(0);
            String to = ticket.get(1);
            if (!graph.containsKey(from)) graph.put(from, new LinkedList<String>());
            graph.get(from).add(to);
        }
        return graph;
    }
}

/**
    !Re - py
    Topological sort: https://www.youtube.com/watch?v=ddTC4Zovtbc
*/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.Stack;

class CourseSchedule2 {
	public int[] findOrder(int numCourses, int[][] prerequisites) {
		if (prerequisites.length < numCourses) {
			return new int[0];
		}

        return bruteForce(numCourses, prerequisites);
    }
	
	private int[] bruteForce(int numCourses, int[][] prerequisites) {
		Set<Integer> visited = new HashSet<>(); 
		Stack<Integer> stack = new Stack<>(); 
		Map<Integer, List<Integer>> graph = createGraph(prerequisites);
		
		for (int key : graph.keySet()) {
			if (visited.contains(key)) {
				continue;
			}
			if(dfs(graph, new HashSet<Integer>(), visited, stack, key)) {
				return new int[0];
			}
		}
		
		return stack.stream().mapToInt(i->i).toArray();
	}
	
	private Boolean dfs(Map<Integer, List<Integer>> graph, Set<Integer> visiting, Set<Integer> visited, Stack<Integer> stack, Integer vertex) {
		visiting.add(vertex);
		visited.add(vertex);

		for (Integer curr : graph.get(vertex)) {
			
			if (visiting.contains(curr)) {
				return true;
			}
			
			if (visited.contains(curr)) {
				continue;
			}
			
			if (dfs(graph, visiting, visited, stack, vertex)) {
				return true;
			}
		}
		
		visiting.remove(vertex);
		stack.add(vertex);
		return false;
	}
	
	private Map<Integer, List<Integer>> createGraph(int[][] prerequisites) {
		Map<Integer, List<Integer>> graph = new HashMap<>();
		
		for (int i = 0; i < prerequisites.length; i++) {
			int start = prerequisites[i][0];
			int end = prerequisites[i][1];
			
			if (graph.containsKey(start)) {
				graph.get(start).add(end);
			} else {
				graph.put(start, new ArrayList<Integer>(end));
			}
		}
		
		return graph;
	}
}

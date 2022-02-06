import java.util.*;

/*
Black bucket
Red bucket


*/
class Solution {
    public boolean solve(int[][] graph) {
        if (graph.length == 0 || graph[0].length == 0) return false;

        Set<Integer> bucket1 = new HashSet<>();
        Set<Integer> bucket2 = new HashSet<>();

        for (int node = 0; node < graph.length; node++) {
            if (isVisited(node, bucket1, bucket2)) continue;
            if (!solve(graph, node, bucket1, bucket2, true)) return false;
        }
        return true;
    }

    private boolean solve(int[][] graph, int node, Set<Integer> bucket1, Set<Integer> bucket2, boolean isBucket1) {
        if (!isValid(node, bucket1, bucket2, isBucket1)) return false;

        if (isBucket1) bucket1.add(node);
        else bucket2.add(node);

        for (int neighbor : graph[node]) {
            if (!isValid(neighbor, bucket1, bucket2, !isBucket1)) return false;
            if (isVisited(neighbor, bucket1, bucket2)) continue;
            if (!solve(graph, neighbor, bucket1, bucket2, !isBucket1)) return false;
        }

        return true;
    }

    private boolean isVisited(int node, Set<Integer> bucket1, Set<Integer> bucket2) {
        return bucket1.contains(node) || bucket2.contains(node);
    }

    private boolean isValid(int node, Set<Integer> bucket1, Set<Integer> bucket2, boolean isBucket1) {
        if (!isVisited(node, bucket1, bucket2)) return true;
        return (isBucket1 && bucket1.contains(node) || !isBucket1 && bucket2.contains(node));
    }
}
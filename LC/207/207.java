class TopologicalSort {
    int count;
    int[] incomings;
    Map<Integer, List<Integer>> graph;
    
    public TopologicalSort(int count, int[][] prereq) {
        this.count = count;
        this.graph = new HashMap<>();
        this.incomings = new int[count];
        
        for (int[] pre : prereq) {
            int target = pre[0];
            int source = pre[1];
            
            if (!this.graph.containsKey(source)) this.graph.put(source, new ArrayList<Integer>());
            this.graph.get(source).add(target);
            this.incomings[target]++;
        }
    }
    
    public List<Integer> sort() {
        List<Integer> sorted = new ArrayList<>();
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < this.incomings.length; i++) {
            if (this.incomings[i] == 0) queue.offer(i);
        }
        
        while (!queue.isEmpty()) {
            int node = queue.poll();
            sorted.add(node);
            
            List<Integer> neighbours = this.graph.getOrDefault(node, new ArrayList<Integer>());
            
            for (int neighbour : neighbours) {
                this.incomings[neighbour]--;
                if (this.incomings[neighbour] == 0) queue.offer(neighbour);
            }
        }
        
        return (sorted.size() != this.count) ? null : sorted;
    }
}

class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        if (numCourses == 0) return prerequisites.length == 0;
        TopologicalSort topo = new TopologicalSort(numCourses, prerequisites);
        return topo.sort() != null;
    }
}

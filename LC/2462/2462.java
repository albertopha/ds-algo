/*
[17, 12, 10, 2, 7, 2, 11, 20, 8 ], k = 3, can = 4
 --  --  --  --    -- --  --  --
 
 PriorityQueue => O(Clog(K))
 
*/
class Solution {
    public long totalCost(int[] costs, int k, int candidates) {
        PriorityQueue<Integer[]> queue = new PriorityQueue<>((a,b) -> {
            if (a[0] == b[0]) return Integer.compare(a[1], b[1]);
            return Integer.compare(a[0], b[0]);
        });
        
        // Fill first candidates
        int start = 0;
        for (int i = 0; i < Math.min(candidates, costs.length); i++) {
            queue.offer(new Integer[]{costs[i], i});
            costs[i] = -1;
            start = i;
        }
        
        // Fill last candidates
        int end = 0;
        for (int i = costs.length-1; i >= Math.max(0, costs.length - candidates); i--) {
            end = i;
            if (costs[i] == -1) break;
            queue.offer(new Integer[]{costs[i], i});
            costs[i] = -1;
        }
        
        long totalCost = 0;
        for (int i = 0; i < k; i++) {
            Integer[] top = queue.poll();
            totalCost += top[0];
            if (top[1] < end && ++start < costs.length && costs[start] > -1) {
                queue.add(new Integer[]{costs[start], start});
                costs[start] = -1;
            }
            else if (top[1] > start && --end >= 0 && costs[end] > -1) {
                queue.add(new Integer[]{costs[end], end});
                costs[end] = -1;
            }
        }
        return totalCost;
    }
}

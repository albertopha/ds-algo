import java.util.*;

class Solution {
    public int solve(int[][] intervals) {
        if (intervals.length == 0) return intervals.length;

        // Sort by the start time
        Arrays.sort(intervals, (interval1, interval2) -> {
            if (interval1[0] == interval2[0]) return interval1[1] - interval2[1];
            return interval1[0] - interval2[0];
        });

        // Priority Queue sorted by the end time
        PriorityQueue<int[]> pq = new PriorityQueue<>((i1, i2) -> i1[1] - i2[1]);
        pq.offer(intervals[0]);

        int size = 1;
        for (int i = 1; i < intervals.length; i++) {
            while (!pq.isEmpty() && pq.peek()[1] <= intervals[i][0]) pq.poll();
            if (pq.isEmpty() || pq.peek()[1] > intervals[i][0]) {
                pq.add(intervals[i]);
            }
            size = Math.max(size, pq.size());
        }

        return size;
    }
}

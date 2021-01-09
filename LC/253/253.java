/*
============================================================
Test case:
#1
[[0, 1], [1, 2], [2, 3]]
-> 1

#2
[[5, 10], [1, 15], [3, 5], [6, 9]]
                             ^
                             ^
[[1,5],[3,5],[5,10],[6,9],[9,12],[9,14]]
          ^

-> overlap = 1
-> maxOverlap = 0

#3
[]
-> 0
============================================================
Brute force:
1. Iterate from i = 1 -> i = 10^4:
    a. count the #overlap.
    b. update the maxOverlap.

Time: O(10^4)
Space: O(1)
============================================================
Brute force:
1. Iterate from i = 0 -> i = intervals.length - 1:
    a. Iterate from j = i + 1 -> intervals.length:
        a. Merge intervals in a way that only overlapped interval
            is retieved.
            ie. [5, 10] and [1, 15] -> [5, 10]

Time: O(N^2)
Space: O(1)
============================================================
Optimal (sort):
1. Sort the intervals by the start time.
2. Initialize the priority queue with first end time.
3. Iterate from i = 1 -> i = intervals.length:
    a. If queue.peek() > intervals[i][0], push end time to queue
        and increment the overlap count.
    b. Pop out queue then push the end time to the queue and
        reset the overlap count to 1.

Time: O(NlogN)
Space: O(N)
============================================================
*/
class Solution {
    public int minMeetingRooms(int[][] intervals) {
        if (intervals == null || intervals.length == 0) {
            return 0;
        }
        
        // Sort by the start time
        Arrays.sort(intervals, new Comparator<int[]>() {
            public int compare(final int[] a, final int[] b) {
                return a[0] - b[0];
            }
        });
        
        // Initialize the priority queue
        PriorityQueue<Integer> pq = new PriorityQueue<>(
            intervals.length,
            new Comparator<Integer>() {
                public int compare(Integer a, Integer b) {
                    return a - b;
                }
            }
        );
        
        pq.add(intervals[0][1]);
        int maxOverlap = 1;
        for (int i = 1; i < intervals.length; i++) {
            while (!pq.isEmpty() && pq.peek() <= intervals[i][0]) {
                pq.poll();
            }
            pq.add(intervals[i][1]);
            maxOverlap = Math.max(maxOverlap, pq.size());
        }
      
        /*************************************************
        OR
        for (int i = 1; i < intervals.length; i++) {
            if (pq.peek() <= intervals[i][0]) {
                pq.poll();
            }
            pq.add(intervals[i][1]);
        }
        return pq.size();
        **************************************************/
        
        return maxOverlap;
    }
}

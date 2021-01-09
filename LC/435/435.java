/*
====================================================================
Test cases:
[[1,2],[2,3],[3,4],[1,3]]
[1,2] -> [1,3]
[2,3] -> [1,3]
[3,4] -> []
[1,3] -> [1,2], [2,3]

[[1,2],[1,3],[2,3],[3,4]]
               ^


[2, 3]

[[2,3],[1,3],[2,4],[3,5]]
[1,2] -> 
====================================================================
====================================================================
Optimal (sort by start + greedy):
1. Sort the intervals by the start time.
2. set prevInterval = first interval.
3. Iterate from i = 1 to intervals.length:
    a. Check if overlapped:
        yes: set prevInterval to interval with the smaller end time.
        no. set prevInterval to current interval and continue.

Time: O(NlogN)
Space: O(1)

if two intervas are overlapping, we want to remove the interval that has the longer end point -- the longer interval will always overlap with more or the same number of future intervals compared to the shorter one
====================================================================
*/

class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        if (intervals == null || intervals.length == 0) {
            return 0;
        }
        
        // Sort by the start time
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        
        int count = 0;
        int[] prevInterval = intervals[0];
        
        for (int i = 1; i < intervals.length; i++) {
            int[] curr = intervals[i];
            
            if (isOverlap(prevInterval, curr)) {
                count++;
                
                // Case 2 and 3
                // 2 -> prevInterval includes currentInterval 
                // 3 -> partially overlaps and end time of the currentInterval is larger
                prevInterval = (prevInterval[1] > curr[1])
                    ? curr
                    : prevInterval;
            } else { // Case 1: no overlap
                prevInterval = curr;
            }
        }
        
        return count;
    }
    
    private boolean isOverlap(int[] source, int[] target) {
        return target[0] < source[1];
    }
}

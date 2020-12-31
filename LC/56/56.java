/*
========================================================
Test cases:

#1
[[1,3],[2,6],[8,10],[15,18]]
                       ^
                       
[[1, 3]]
    ^
[[1, 6]]
    ^
[[1, 6], [8, 10]]
            ^
[[1, 6], [8, 10], [15, 18]]
                      ^
#2
[[]]
[]

========================================================
Brute force:
1. Iterate through the list from i = 0 to end of the list:
    a. Iterate from j = i to end of the list:
        (i) record start and end intervals
        (ii) on each iteration, check if the interval is
            within the current interval.
            ie. interval[j][0] <= end and interval[j][1] >= start
            if so, set start = min(interval[j][0], start)
            and end = max(interval[j][1], end)
    b. Once iteration is completed, add [start, end] to the result array

Time: O(N^2), N = length of the array
Space: O(1)
========================================================
Optimal in terms of time complexity:
1. Sort the intervals by the start time.  --- O(NlogN)
2. Iterate from i = 0 to end of the list, --- O(N)
    merge intervals on each step.
    
Time: O(NlogN)
Space: O(NlogN)
========================================================

*/
class Solution {
    public int[][] merge(int[][] intervals) {
        // Sort by the start time
        Arrays.sort(intervals, Comparator.comparingInt(o -> o[0]));
        List<int[]> result = new ArrayList<>();
        
        int resultInd = 0;
        result.add(intervals[0]);
        for (int i = 0; i < intervals.length; i++) {
            int prevStartTime = result.get(resultInd)[0];
            int prevEndTime = result.get(resultInd)[1];
            int startTime = intervals[i][0];
            int endTime = intervals[i][1];
            
            if (startTime <= prevEndTime) {
                result.get(resultInd)[0] = Math.min(prevStartTime, startTime);
                result.get(resultInd)[1] = Math.max(prevEndTime, endTime);
            } else {
                result.add(intervals[i]);
                resultInd++;
            }
        }

        return result.toArray(new int[result.size()][]);
    }
}
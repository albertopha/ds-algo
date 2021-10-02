/*
// Definition for an Interval.
class Interval {
    public int start;
    public int end;

    public Interval() {}

    public Interval(int _start, int _end) {
        start = _start;
        end = _end;
    }
};

[1,2], [5,6]
[1,3]
=> [1,3], [5,6]
[4,10]
=> [1,3], [4,10]
=> [3,4]
*/

class Solution {
    public List<Interval> employeeFreeTime(List<List<Interval>> schedule) {
        if (schedule.size() == 0 || schedule.get(0).size() == 0) return null;
        List<Interval> flattened = flattenIntervals(schedule);
        List<Interval> merged = mergeIntervals(flattened);
        return findFreeTimes(merged);
    }
    
    private List<Interval> flattenIntervals(List<List<Interval>> schedule) {
        List<Interval> flattened = new ArrayList<>();
        for (List<Interval> intervals: schedule) {
            flattened.addAll(intervals);
        }
        flattened.sort((interval1, interval2) -> {
            if (interval1.start == interval2.start) return interval1.end - interval2.end;
            return interval1.start - interval2.start;
        });
        return flattened;
    }
    
    private List<Interval> mergeIntervals(List<Interval> intervals) {
        List<Interval> merged = new ArrayList<>();
        merged.add(intervals.get(0));
        int mergedIdx = 0;
        for (int i = 1; i < intervals.size(); i++) {
            int start = intervals.get(i).start;
            int end = intervals.get(i).end;
            int mergedStart = merged.get(mergedIdx).start;
            int mergedEnd = merged.get(mergedIdx).end;
            
            if (start <= mergedEnd) {
                merged.set(mergedIdx, new Interval(Math.min(start, mergedStart), Math.max(end, mergedEnd)));
            } else {
                merged.add(intervals.get(i));
                mergedIdx++;
            }
        }
        
        return merged;
    }
    
    private List<Interval> findFreeTimes(List<Interval> intervals) {
        List<Interval> freeTimes = new ArrayList<>();
        for (int i = 1; i < intervals.size(); i++) {
            int prevEnd = intervals.get(i-1).end;
            int currStart = intervals.get(i).start;
            freeTimes.add(new Interval(prevEnd, currStart));
        }
        return freeTimes;
    }
}
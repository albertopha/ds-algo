class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals or len(intervals) == 1:
            return intervals
        
        # Sort by the start time
        return self.greedy(sorted(intervals, key=lambda x: x[0]))
    
    def greedy(self, intervals):
        result = []
        merged_interval = intervals[0]
        
        for ind, interval in enumerate(intervals):
            start, end = interval
            if start > merged_interval[1]:
                result.append(merged_interval)
                merged_interval = interval
            else:
                merged_interval[0] = min(start, merged_interval[0])
               merged_interval[1] = max(end, merged_interval[1])
        
        result.append(merged_interval)
        
        return result
 

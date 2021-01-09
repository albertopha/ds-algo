"""
========================================================
Test cases:
#1
[[1,0], [0,2]], k = 1
-> [[1,0]]

#2
[[-5,-5],[1,2],[2,4],[-6,8]], k = 2
[sqrt(50), sqrt(5), sqrt(20), sqrt(100)]
                       p
[2, 1, 2, 2, 6, 10, 9, 8]
             i
                    j

-> [[1,2],[2,4]]
========================================================
Brute force:
1. Initialize variable max_dist_ind = 0; and result array = []
2. While k > 0: --- O(K)
    a. Iterate from i = 0 to len(points): --- O(P)
        a. calculate the distance and update max_dist_ind.
    b. push points[max_dist_ind] into result array.
    c. remove the point at max_dist_ind from the points array. --- O(K)
    d. k -= 1

Time: O(K*(P+K))
Space: O(K)
=======================================================
Sub-optimal (min-heap):
1. return K closest points to origin using heapq.nsmallest

Time: O(NlogK)
Space: O(K)
========================================================
Optimal (quick select):
1. Perform quick select algorithm

Time: O(N) in avg, O(N^2) in the worst case
Space: O(1)
========================================================
"""
import heapq
import math

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        if not points or K > len(points):
            return []
        
        self.kClosestQuickSelect(points, 0, len(points) - 1, K)
        return points[:K]
    
    def kClosestQuickSelect(self, points, start, end, K):
        if start >= end:
            return
        
        pivot = self.partition(points, start, end)
        
        if K == pivot:
            return
        
        if K < pivot:
            self.kClosestQuickSelect(points, start, pivot - 1, K)
        else:
            self.kClosestQuickSelect(points, pivot + 1, end, K)
                
    def partition(self, points, start, end):
        i, pivot = start, self.euclideanDist(points[end])
        
        for j in range(start, end):
            curr = self.euclideanDist(points[j])
            if curr < pivot:
                points[j], points[i] = points[i], points[j]
                i += 1
                
        points[i], points[end] = points[end], points[i]
        return i
    
    def euclideanDist(self, point):
        return math.sqrt(point[0] ** 2 + point[1] ** 2)
    
    
    def kClosestHeap(self, points, K):
        if not points or K > len(points):
            return []
        
        return heapq.nsmallest(K, points, key=lambda p: p[0]**2+p[1]**2)
        

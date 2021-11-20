"""
[9,4,2,10,7,8,8,1,9]
 ^
     ^
flag = -1
"""
class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) <= 1:
            return len(arr)
        
        s, max_len = 0, 1
        for e in range(1, len(arr)):
            compare = cmp(arr[e-1], arr[e])
            
            # Same value found, skip
            if compare == 0:
                s = e
                continue
            
            if e == len(arr)-1 or compare * cmp(arr[e], arr[e+1]) != -1:
                max_len = max(max_len, (e - s + 1))
                s = e
        return max_len

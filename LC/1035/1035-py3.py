"""
[1,4,2]
 ^
[1,2,4]
 ^

[1,2,3,4,5]
 ^
[1,3,4,5,2]
 ^
"""
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        if not nums1 or not nums2:
            return 0

        def recursion(index1: int, index2: int, memo: List[List[int]]) -> int:
            if index1 >= len(nums1) or index2 >= len(nums2):
                return 0
            
            if memo[index1][index2] != None:
                return memo[index1][index2]
            
            if nums1[index1] == nums2[index2]:
                memo[index1][index2] = max(
                    recursion(index1+1, index2, memo),
                    1 + recursion(index1+1, index2+1, memo)
                )
                return memo[index1][index2]
            
            memo[index1][index2] = max(
                recursion(index1+1, index2, memo),
                recursion(index1, index2+1, memo)
            ) 
            return memo[index1][index2]
        
        memo = [[None for _ in range(len(nums2))] for _ in range(len(nums1))]
        return recursion(0, 0, memo)

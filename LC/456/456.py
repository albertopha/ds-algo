"""
============================================================
Test cases:
#1
[1, 2, 3, 4]
-> False

#2
[4, 3, 2, 1]
-> False

#3
[4, 6, 5, 3, 5]
 i
          j
 
1 -> 5 -> 10 -> 3
stack = [1, 5, 3]
-> True

#4
[1, 2]
-> False
============================================================
Brute force:
1. Iterate through the array from i = 0 to i = len(arr) - 3:
    a. iterate from j = i + 1 to len(arr) - 2:
        a. k = j + 1 to len(arr) - 1:
            a. check if it's 132 pattern

Time: O(N^3)
Space: O(1)
============================================================
Sub-optimal:
1. Iterate from i = 0 to i = len(arr) - 3:
    a. look for the value greater than arr[i].
    a. look for the peek (return true if there's time when the value decreses)

Tme: O(N^2)
Space: O(1)
============================================================
Optimal:
1. Initialize an array that contains the minimum value
    seen so far up to the index of i.
2. Use stack and traverse from j = len(arr) to j = 0:
    a. while arr[j] > stack.peek():
        check if stack.peek() > min[j]:
            return true if it is
            else stack.pop()
    b. stack.push(arr[j])

Time: O(N)
Space: O(N)
============================================================
"""
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        
        return self.optimal(nums)
        
    def optimal(self, nums):
        mins = nums[:]
        stack = []
        
        for i in range(1, len(mins)):
            mins[i] = min(mins[i], mins[i-1])
        
        for j in range(len(nums)-1, 0, -1):
            while stack and stack[-1] < nums[j]:
                if stack[-1] > mins[j]:
                    return True
                
                stack.pop()
            
            stack.append(nums[j])
        
        return False
    
    def subOptimal(self, nums):
        
        for i in range(len(nums) - 2):
            j = i + 1
            
            while nums[j] <= nums[i] and j < len(nums) - 1:
                j += 1
                
            if j > len(nums) - 2:
                continue

            peek = nums[j]
            for k in range(j, len(nums)):
                if nums[i] < nums[k] < peek:
                    return True
                peek = max(peek, nums[k])
        
        return False


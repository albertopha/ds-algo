class QuickSelect:

    def __init__(self):
        pass

    def select(self, nums, start, end, position):
        if start > end:
            return nums[start]
        
        pivot = self.partition(nums, start, end)

        if pivot == position:
            return nums[pivot]
        
        if pivot < position:
            return self.select(nums, pivot+1, end, position)

        return self.select(nums, start, pivot-1, position)

    def partition(self, nums, start, end):
        prev, pivot = start, end
        for i in range(start, pivot):
            if nums[i] < nums[pivot]:
                nums[prev], nums[i] = nums[i], nums[prev]
                prev += 1
        
        nums[prev], nums[pivot] = nums[pivot], nums[prev]
        return prev

class Solution:
    def solve(self, nums, k):
        if not nums or len(nums) < k:
            return 0
        
        qs = QuickSelect()
        return qs.select(nums, 0, len(nums)-1, k)

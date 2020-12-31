#!
class Solution(object):
    def nextPermutation(self, nums):
        is_ascending, ind1, ind2 = self.ascending(nums)

        if is_ascending:
            self.reverse_list(nums)
            return

        minInd = ind2
        for i in range(ind2, len(nums)):
            if nums[i] > nums[ind1] and nums[i] <= nums[minInd]:
                minInd = i

        nums[ind1], nums[minInd] = nums[minInd], nums[ind1]
        self.reverse_list(nums, ind2)

        return nums

    @staticmethod
    def ascending(nums):
        ind = len(nums)-1

        while ind > 0:
            if nums[ind-1] < nums[ind]:
                return False, ind-1, ind
            ind -= 1

        return True, -1, -1

    @staticmethod
    def reverse_list(nums, s=0):
        start, end = s, len(nums)-1

        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


    def nextPermutation_brute(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if self.isAscending(nums):
            return nums[::-1]

        p = len(nums)-2
        while 1:
            p1 = len(nums)-1
            nextNums = nums[:]
            while p1 > p:
                nextNums[p1], nextNums[p1-1] = nextNums[p1-1], nextNums[p1]
                if self.isNextPermutation(nums, nextNums):
                    return nextNums
                p1 -= 1
            p -= 1

    @staticmethod
    def isAscending(nums):
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                return False
        return True

    @staticmethod
    def isNextPermutation(nums, nextNums):
        for i in range(len(nums)):
            if nums[i] < nextNums[i]:
                return True
            if nums[i] > nextNums[i]:
                return False
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isNextPermutation([1, 3, 2], [1, 2, 3]))
    print(s.isNextPermutation([1, 3, 2], [1, 3, 2]))
    print(s.isNextPermutation([1, 3, 2], [2, 3, 1]))
    print(s.isNextPermutation([1, 2, 3], [1, 3, 2]))

    print(s.nextPermutation([1, 2, 3]))
    print(s.nextPermutation([1, 3, 2]))
    print(s.nextPermutation([2, 3, 1]))
    print(s.nextPermutation([5, 4, 7, 5, 3, 2]))
    print(s.nextPermutation([2,3,1,3,3]))

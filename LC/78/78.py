# !
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result_brute = []
        result_opt = []
        self.subsets_brute_rec(nums, result_brute)
        self.subsets_opt(nums, result_opt, [], 0)

        print('brute -> ')
        print(result_brute)

        print('opt -> ')
        print(result_opt)

    def subsets_opt(self, nums, result, temp, start):
        result.append(temp[:])

        for i in range(start, len(nums)):
            temp.append(nums[i])
            self.subsets_opt(nums, result, temp, i+1)
            temp.pop(len(temp)-1)

    def subsets_brute_rec(self, nums, result):
        if len(nums) == 0:
            return

        if nums not in result:
            result.append(nums)

        for i in range(len(nums)):
            if i == 0:
                self.subsets_brute_rec(nums[1:], result)
            elif i == len(nums)-1:
                self.subsets_brute_rec(nums[0:-1], result)
            else:
                self.subsets_brute_rec(nums[0:i] + nums[i+1:], result)



if __name__ == '__main__':
    s = Solution()
    s.subsets([1, 2, 3])
    s.subsets([1,2,3,4,5,6,7,8,10,0])

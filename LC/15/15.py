# !
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []

        result = []
        nums.sort()

        for i in range(len(nums)-2):
            curr = nums[i]
            start = i+1
            end = len(nums)-1

            if i > 0 and curr == nums[i-1]:
                continue

            while start < end:
                if curr + nums[start] + nums[end] == 0:
                    result.append([curr, nums[start], nums[end]])
                    while start < end and nums[start] == nums[start+1]:
                        start += 1
                    while start < end and nums[end] == nums[end-1]:
                        end -= 1
                    start += 1
                    end -= 1
                elif curr + nums[start] + nums[end] < 0:
                    start += 1
                else:
                    end -= 1

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
    print(s.threeSum([0, 0, 0, 0]))
    print(s.threeSum([-2, 0, 1, 1, 2]))
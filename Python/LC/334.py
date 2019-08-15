import sys
from typing import List

# ! Re - J
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        return self.opt_increasing_triplet(nums)

    @staticmethod
    def opt_increasing_triplet(nums: List[int]) -> bool:
        small, big = sys.maxsize, sys.maxsize

        for n in nums:
            if n <= small:
                small = n
            elif n <= big:
                big = n
            else:
                return True

        return False


if __name__ == '__main__':
    s = Solution()
    print(s.increasingTriplet([1,2,3,5]))
    print(s.increasingTriplet([5,4,3,2,1]))
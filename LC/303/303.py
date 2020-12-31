from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        for i in range(len(self.nums)):
            if i > 0:
                self.nums[i] += self.nums[i-1]
        print(self.nums)

    def sumRange(self, i: int, j: int) -> int:
        if i > 0:
            return self.nums[j] - self.nums[i - 1]

        return self.nums[j]


if __name__ == '__main__':
    n = NumArray([-2, 0, 3, -5, 2, -1])
    print(n.sumRange(0, 2))
    print(n.sumRange(1, 3))
    print(n.sumRange(2, 5))
    print(n.sumRange(0, 5))

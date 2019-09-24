# ! - J (Fenwick's tree, segment tree)
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.original_nums = list(nums)
        self.nums = nums
        for i in range(len(nums)):
            if i == 0:
                self.nums[i] = nums[i]
            else:
                self.nums[i] += nums[i-1]

    def update(self, i: int, val: int) -> None:
        diff = val - self.original_nums[i]
        self.original_nums[i] = val
        self.resetNums(i, diff)

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.nums[j]
        return self.nums[j] - self.nums[i - 1]

    def resetNums(self, startInd: int, diff: int) -> None:
        for i in range(startInd, len(self.nums)):
            self.nums[i] += diff


if __name__ == '__main__':
    n = NumArray([1, 3, 5])
    print(n.sumRange(0, 2))
    n.update(1, 2)
    print(n.sumRange(0, 2))
    n.update(2, 10)
    print(n.sumRange(0, 2))

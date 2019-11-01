from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # return self.brute_force(nums)
        return self.optimal(nums)

    def optimal(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1

        return i

    def brute_force(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        start, count, search, new_length = 0, 0, 0, len(nums)

        while search < new_length:
            count = 0
            # print('start -> ', start)
            # print('search -> ', search)
            # print('new_length -> ', new_length)

            while search < new_length and nums[start] == nums[search]:
                count += 1
                search += 1

            # print('after dup: search -> ', search)
            # print('after dup: count -> ', count)

            if count > 2:
                num_dup = count - 2
                for current in range(search, new_length):
                    nums[current-num_dup] = nums[current]

                new_length -= num_dup
                search -= num_dup

            start = search
        return new_length


if __name__ == '__main__':
    s = Solution()
    a = [1,1,1,2,2,3]
    a_len = s.removeDuplicates(a)
    print(a_len)
    print('a -> ', a[:a_len])

    a1 = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3]
    a1_len = s.removeDuplicates(a1)
    print(a1_len)
    print('a -> ', a1[:a1_len])

    a2 = [0,0,1,1,1,1,2,3,3]
    a2_len = s.removeDuplicates(a2)
    print(a2_len)
    print('a2 -> ', a2[:a2_len])

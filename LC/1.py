class TwoSum(object):
    @staticmethod
    def two_sum_brute(nums, target):
        for i in range(len(nums)-1):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

            return []

    @staticmethod
    def two_sum_opt(nums, target):
        hash = {}
        for i in range(len(nums)):
            if nums[i] in hash:
                return [hash[nums[i]], i]

            diff = target - nums[i]
            hash[diff] = i

        return []


if __name__ == '__main__':
    ts = TwoSum()
    print(ts.two_sum_brute([2, 7, 11, 15], 9))
    print(ts.two_sum_opt([2, 7, 11, 15], 9))
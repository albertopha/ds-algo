class Solution(object):
    def find_magic_index(self, arr):
        if not arr:
            return -1

        return self.distinct_integer(arr)

    @staticmethod
    def distinct_integer(arr):
        start, end = 0, len(arr)-1

        while start <= end:
            mid = (start + end) // 2
            if mid == arr[mid]:
                return mid

            if mid > arr[mid]:
                start = mid + 1
            else:
                end = mid - 1

        return -1

    @staticmethod
    def non_distinct_interger(arr):


if __name__ == '__main__':
    s = Solution()
    print(s.find_magic_index([1, 2, 3, 4, 5, 6]))
    print(s.find_magic_index([-1, 0, 1, 2, 4, 10]))
    print(s.find_magic_index([-5, 1, 3, 4, 5, 10]))


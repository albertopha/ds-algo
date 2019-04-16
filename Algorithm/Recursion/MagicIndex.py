#! non_distinct
class MagicIndex:
    def __init__(self):
        return

    @staticmethod
    def magic_index_brute_force(arr):
        for i in range(len(arr)):
            if arr[i] > i:
                return -1

            if i == arr[i]:
                return i

        return -1

    @staticmethod
    def magic_index_binary_search(arr):
        start = 0
        end = len(arr) - 1
        index = -1

        if start == end:
            return start if arr[start] == start else -1

        while start < end:
            half = (start + end) / 2

            if arr[half] == half:
                index = half
                end = half
            elif arr[half] > half:
                end = half
            else:
                start = half+1

        return index

    def magic_index_non_distinct(self, arr, start, end):
        mid = (start + end) / 2

        if start > end:
            return -1

        if arr[mid] == mid:
            return mid

        left = self.magic_index_non_distinct(arr, start, min(mid-1, arr[mid]))
        if left >= 0:
            return left

        right = self.magic_index_non_distinct(arr, max(mid+1, arr[mid]), end)
        return right


if __name__ == '__main__':
    mi = MagicIndex()

    print("Brute Force: ")
    print(mi.magic_index_brute_force([0]))
    print(mi.magic_index_brute_force([-1]))
    print(mi.magic_index_brute_force([-1, 0, 2, 3]))
    print(mi.magic_index_brute_force([-1, 0, 2, 3]))

    print("\nBinary Search: ")
    print(mi.magic_index_binary_search([0]))
    print(mi.magic_index_binary_search([-1]))
    print(mi.magic_index_binary_search([-1, 0, 2, 3]))
    print(mi.magic_index_binary_search([-1, 0, 2, 3]))

    print("\nNon distinct: ")
    print(mi.magic_index_non_distinct([-10, -5, 2, 2, 2, 3, 4, 8, 9, 12, 13], 0, 10))

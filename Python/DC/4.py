# ! dc-4 and lc-41
# [1,2,0] -> [2,1,0] -> [0,1,2] -> 3
# [3,4,-1,1] -> [1,4,-1,3] -> [4,1,-1,3] -> [1,4,-1,3]  -> 2
# [7,8,9,11,12] -> [7,8,9,11,12]


class DC4(object):
    @staticmethod
    def missing_int_brute(arr):
        if len(arr) == 0:
            return

        arr.sort()
        for i in range(len(arr)-1):
            if arr[i] < 0:
                continue

            if arr[i] + 1 != arr[i+1]:
                return arr[i] + 1

        return arr[-1]+1

    @staticmethod
    def missing_int(arr):
        if len(arr) == 0:
            return 1

        m = max(arr)

        if m < 0:
            return 1

        if len(arr) == 1:
            if arr[0] == 1:
                return 2
            else:
                return 1

        i = 0
        arr.append(-1)
        while i < len(arr):
            curr = arr[i]
            if curr >= len(arr) or curr < 0:
                i += 1
                continue
            if i != curr and arr[i] != arr[curr]:
                arr[curr], arr[i] = curr, arr[curr]
                continue

            i += 1

        for i in range(1, len(arr)):
            if i != arr[i]:
                return i

        return len(arr)


if __name__ == '__main__':
    dc4 = DC4()
    print(dc4.missing_int_brute([3, 4, -1, 1]))
    print(dc4.missing_int_brute([1, 2, 0]))
    print(dc4.missing_int([3, 4, -1, 1]))
    print(dc4.missing_int([1, 2, 0]))
    print(dc4.missing_int([3, 4, -1, 1]))
    print(dc4.missing_int([3, 4, 2, 1]))
    print(dc4.missing_int([7, 8, 9, 11, 12]))
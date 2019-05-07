#! follow up
class DC2(object):
    @staticmethod
    def dc2_opt(arr):
        mul = 1

        for n in arr:
            mul *= n

        return [mul/i for i in arr]

    @staticmethod
    def dc2_follow_up(arr):
        left, right = [1 for _ in range(len(arr))], [1 for _ in range(len(arr))]

        if len(arr) < 2:
            return 0

        for i in range(len(arr)):
            if i > 0:
                left[i] = left[i-1] * arr[i-1]

        for i in range(len(arr)-1, -1, -1):
            if i < len(arr)-1:
                right[i] = right[i+1] * arr[i+1]

        return [left[i]*right[i] for i in range(len(arr))]


if __name__ == '__main__':
    dc2 = DC2()
    print(dc2.dc2_opt([1, 2, 3, 4, 5]))
    print(dc2.dc2_opt([3, 2, 1]))

    print(dc2.dc2_follow_up([1, 2, 3, 4, 5]))
    print(dc2.dc2_follow_up([3, 2, 1]))


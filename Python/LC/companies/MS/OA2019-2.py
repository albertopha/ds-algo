class Solution(object):
    def solution(self, N: int) -> int:
        if N == 0:
            return 50

        arr = self.toArr(abs(N))

        sign = 1 if N >= 0 else 0
        ind = 0
        inserted = False

        while ind < len(arr):
            if sign:
                if 5 > arr[ind]:
                    arr.insert(ind, 5)
                    inserted = True
                    break
            else:
                if 5 < arr[ind]:
                    arr.insert(ind, 5)
                    inserted = True
                    break
            ind += 1

        if not inserted:
            arr.append(5)
        return self.toInt(arr) * (1 if sign else -1)

    def toArr(self, n):
        arr = []

        while n > 0:
            arr.insert(0, n % 10)
            n //= 10

        return arr

    def toInt(self, arr) -> int:
        n = 0

        for i in arr:
            n *= 10
            n += i

        return n


if __name__ == '__main__':
    s = Solution()
    print(s.solution(268))
    print(s.solution(670))
    print(s.solution(0))
    print(s.solution(-999))
    print(s.solution(9))


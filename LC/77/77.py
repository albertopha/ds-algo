# !Re - J
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        if k == 0:
            return result

        self.brute_force(n, k, 0, [], result)

        return result

    def brute_force(self, n: int, k: int, start: int, curr: List[int], l: List[List[int]]) -> List[List[int]]:
        if k == 0:
            l.append(curr[:])
            return

        for i in range(start, n):
            curr.append(i+1)

            if i+1 <= n:
                self.brute_force(n, k-1, i+1, curr, l)

            curr.pop()


if __name__ == '__main__':
    s = Solution()
    print(s.combine(4, 2))
    print(s.combine(4, 3))
    print(s.combine(4, 4))

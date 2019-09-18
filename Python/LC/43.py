#! - J
import math


class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 is "" or num2 is "":
            return ""

        if num1 == "0" or num2 == "0":
            return "0"

        multiplied = [""]*(len(num1)+len(num2))

        for ind2 in range(len(num2)-1, -1, -1):
            for ind1 in range(len(num1)-1, -1, -1):
                p1, p2 = ind1+ind2, ind1+ind2+1
                curr = int(num2[ind2]) * int(num1[ind1])
                curr += multiplied[p2] if multiplied[p2] is not "" else 0
                multiplied[p2] = curr % 10

                if multiplied[p1] is not "":
                    multiplied[p1] += math.floor(curr / 10)
                elif math.floor(curr / 10) > 0:
                    multiplied[p1] = math.floor(curr / 10)

        return "".join(str(x) for x in multiplied)


if __name__ == '__main__':
    s = Solution()
    print(s.multiply("1", "23"))

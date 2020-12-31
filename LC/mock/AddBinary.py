import math


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        flag = 0
        a_list = list(a)
        a_list.reverse()
        b_list = list(b)
        b_list.reverse()
        longer = max(len(a), len(b))

        for i in range(longer):
            curr = 0

            if i < len(a_list):
                curr = int(a_list[i])

            if i < len(b_list):
                curr += int(b_list[i])

            curr += flag

            flag = math.floor(curr / 2)
            curr %= 2

            result.append(str(curr))

        if flag:
            result.append(str(flag))

        result.reverse()
        return "".join(result)
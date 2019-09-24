class Solution(object):
    def __init__(self):
        self.days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def solution(self, s: str, K: int) -> str:
        if K < 0 or K > 500:
            return ""
        ind = (K + self.days_of_week.index(s)) % 7
        return self.days_of_week[ind]


if __name__ == '__main__':
    s = Solution()
    print(s.solution("Wed", 2))
    print(s.solution("Sat", 23))

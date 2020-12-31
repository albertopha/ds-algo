class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        return self.brute_force(s)

    def brute_force(self, s: str) -> int:
        return -1


if __name__ == '__main__':
        s = Solution()
        print(s.lengthOfLongestSubstring('abrkaabcdefghijjxxx')) # 10

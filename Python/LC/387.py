class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash = {}

        for i in range(len(s)):
            curr = s[i]
            if curr in hash:
                hash[curr] = -1
            else:
                hash[curr] = i

        for i in hash.values():
            if i != -1:
                return i

        return -1
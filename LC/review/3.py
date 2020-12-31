#! optimized
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        longest = 0
        start, i = 0, 0

        if len(s) < 2:
            return len(s)

        while i < len(s):
            ch = s[i]

            if ch not in hashmap:
                hashmap[ch] = i
                i += 1
                longest = max(longest, i - start)
            else:
                dup = s[start]
                start += 1
                del hashmap[dup]
        return longest

###########################################################
#
# Given a string, find the length of the longest
# substring in it with no more than K distinct characters.
###########################################################
from collections import defaultdict

def findLongestSubstrLengthKDistinct(s, k):
    if not s:
        return 0

    left = 0
    unique_count = 0
    char_map = defaultdict(lambda: 0)
    max_len = 0

    for right in range(len(s)):
        if char_map[s[right]] == 0:
            unique_count += 1
        char_map[s[right]] += 1

        while left < right and unique_count > k:
            char_map[s[left]] -= 1

            if char_map[s[left]] == 0:
                unique_count -= 1

            left += 1
        
        max_len = max(max_len, (right - left + 1))
    return max_len


if __name__ == "__main__":
    s = "araaci"
    k = 2
    print(findLongestSubstrLengthKDistinct(s, k))
    
    s = "araaci"
    k = 1
    print(findLongestSubstrLengthKDistinct(s, k))

    s = "cbbebi"
    k = 3
    print(findLongestSubstrLengthKDistinct(s, k))


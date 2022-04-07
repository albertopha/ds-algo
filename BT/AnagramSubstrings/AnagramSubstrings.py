"""
"abca"
 ^
"bcabxabca"
  ^
      ^

{
    a: 2,
    b: 1,
    c: 0,
    x: 1
}

unique = 2
"""
from collections import Counter
class Solution:
    def solve(self, s0, s1):
        if not s0 or not s1:
            return 0
        
        count = 0
        counter = Counter(s0)
        bucket = [0] * 26

        l = 0
        for r in range(len(s1)):
            bucket[ord(s1[r])-ord('a')] += 1

            if s1[r] not in counter:
                while l <= r:
                    bucket[ord(s1[l])-ord('a')] -= 1
                    l += 1
                continue

            if self.isValid(counter, bucket):
                bucket[ord(s1[l])-ord('a')] -= 1
                l += 1
                count += 1
        
        while l < len(s1):
            bucket[ord(s1[l])-ord('a')] -= 1
            if self.isValid(counter, bucket):
                count += 1
            l += 1

        return count
    
    def isValid(self, counter, bucket):
        for key, count in counter.items():
            if bucket[ord(key)-ord('a')] != count:
                return False
        return True

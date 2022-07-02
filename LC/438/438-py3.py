"""
cbaebabacd,  abc
      ^
       ^

{
    a: 1
    b: 1
}

"ababababab"
   ^
    ^
"aab"

{
    a: 1,
    b: 1
}


"vwwvv"
   ^
     ^
"vwv"

{
    v: 0
    w: 1
}
"""

from collections import Counter, defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or not p:
            return []
        
        p_counter = Counter(p)
        counter = defaultdict(lambda: 0)
        l, unique_count = 0, 0
        anagrams = []
        
        for r, char in enumerate(s):
            if char not in p_counter:
                l = r + 1
                counter.clear()
                unique_count = 0
                continue
            
            counter[char] += 1
            if counter[char] == p_counter[char]:
                unique_count += 1
            
            while l < r and counter[char] > p_counter[char]:
                prev_state = counter[s[l]] == p_counter[s[l]]
                counter[s[l]] -= 1
                if prev_state and counter[s[l]] < p_counter[s[l]]:
                    unique_count -= 1
                l += 1
            
            if unique_count == len(p_counter):
                anagrams.append(l)
            
        return anagrams
            
        
        

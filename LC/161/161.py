"""
ab, acb
 ^    ^
 
""  ""

"a" ""
 ^   
 
"""
class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if abs(len(s) - len(t)) > 1:
            return False
        
        if len(s) > len(t):
            return self.isOneEditDistance(t, s)
        
        is_diff = False
        si, ti = 0, 0
        while ti < len(t):
            if si >= len(s) or s[si] != t[ti]:
                if is_diff:
                    return False
                is_diff = True
                if len(s) == len(t):
                    si += 1
                ti += 1
            else:
                si += 1
                ti += 1
        return is_diff


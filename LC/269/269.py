"""
["wrt","wrf","er","ett","rftt"]

Since the words are sorted lexicographically, we can
compare word[i] with word[i+1]. 

ie. w1 = "wrt" vs w2 = "wrf"
index = 0
w1[index] = "w", w2[index] = "w"
same -> continue

index = 1
w1[index] = "r", w2[index] = "r"
same -> continue

index = 2
w1[index] = "t", w2[index] = "f"
at this point, we know t should come before f ("t" -> "f")
"""
from collections import deque

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if not words:
            return ""
        
        # graph needs to be an list instead of set()
        # as there can be duplicate in_degree
        # ie. ["ac","ab","zc","zb"]
        # "c" -> "b"
         If set is used, must check:
        # if target not in graph[source]:
        graph = defaultdict(lambda: [])
        in_degree = dict()
        
        for word in words:
            for char in word:
                in_degree[char] = 0
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            
            ind = 0
            while ind < min(len(w1), len(w2)):
                if w1[ind] != w2[ind]:
                    graph[w1[ind]].append(w2[ind])
                    in_degree[w2[ind]] += 1
                    break
                ind += 1
            else:
                # This is only called when the condition of the
                # while loop is false. We don't want this to be
                # called when while loop terminates due to "break" statement.
                # check that w2 is not a prefix of w1
                # ie. ["abc","ab"]
                # Clearly "ab" is not a prefix of "abc".
                # without the check, it will return "acb".
                if len(w1) > len(w2):
                    return ""
        
        output = []
        queue = list(filter(lambda c: in_degree[c] == 0, in_degree))
        
        while queue:
            char = queue.pop(0)
            output.append(char)
            
            for next_char in graph[char]:
                in_degree[next_char] -= 1
                if in_degree[next_char] == 0:
                    queue.append(next_char)
        
        if len(output) != len(in_degree):
            return ""
        return "".join(output)

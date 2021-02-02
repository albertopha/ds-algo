"""
["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
                ^
["root/a", "1.txt(abcd)", "2.txt(efgh)"]
                ^             
extract content -> indexOf("(") - lastInd
[
    "abcd": set("root/a/1.txt"),
    "efgh": set("root/a/2.txt")
]

====================================================================================
Brute force:
1. Iterate from i = 0 to len(paths): --- O(P)
    a. For each path, split by the blank space, " " --- O(1)
    b. Iterate the splitted array starting at i = 1 to end of the array: --- O(1)
        a. Extract the content and save it into the dict
        b. Extract the current file path from the root and add it to the dict
2. Get the list of values of themap and return the result array

Time: O(P)
Space: O(P)
====================================================================================

====================================================================================
"""
from collections import defaultdict

class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        if not paths:
            return []
        
        content_dict = defaultdict(set)
        
        for path in paths:
            path_split = path.split(" ")
            
            if len(path_split) <= 1:
                continue
            
            dir_path = path_split[0]
            for j in range(1, len(path_split)):
                name, content = self.extract(path_split[j])
                pwd = dir_path + "/" + name
                content_dict[content].add(pwd)
            
        result = []
        for value in content_dict.values():
            if (len(value) > 1):
                result.append(list(value))
        
        return result
    
    def extract(self, f):
        start = f.index("(")
        end = len(f)
        
        return f[0:start], f[start:end]
             

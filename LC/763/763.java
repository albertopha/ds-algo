/*
================================================================
Test cases:
#1:
"ababcbacadefegdehijhklij"
                ^
                ^
================================================================
Brute force:
================================================================
Optimal solution:
1. Initialize Map<Character, Integer> where map will save
    the character from S as a key and index as a value.
2. Iterate from i = 0 to i = S.length():
    a. Keep inputting the current character with the current index.
3. Iterate from i = 0 to i = S.length():
    a. Record the start position, int start = i
    b. From j = i to j = S.length():
        a. Move i to map.get(S.charAt(j))
        b. If i == j, break the for loop
    c. Push the ith (ndex - start + 1) to result array

Time: O(N)
Space: O(1), 26 alphabets
================================================================
*/
class Solution {
    public List<Integer> partitionLabels(String S) {
        List<Integer> result = new ArrayList<>();
        if (S == null || S.length() == 0) {
            return result;
        }
        
        // Create map
        Map<Character, Integer> map = new HashMap<>();
        
        for (int i = 0; i < S.length(); i++) {
            map.put(S.charAt(i), i);
        }
        
        int i = 0;
        while (i < S.length()) {
            int start = i;
            int j = i;
            
            i = map.get(S.charAt(i));
            
            while (j < i) {
                i = Math.max(i, map.get(S.charAt(j)));
                j++;
            }
            
            result.add(i - start + 1);
            i++;
        }
        
        return result;
    }
}

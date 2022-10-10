class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> output = new ArrayList<>();
        if (strs.length == 0) return output;
        
        Map<String, List<String>> map = new HashMap<>();
        for (int i = 0; i < strs.length; i++) {
            String key = this.getKey(strs[i]);
            if (!map.containsKey(key)) map.put(key, new ArrayList<String>());
            map.get(key).add(strs[i]);
        } 
        
        for (List<String> value: map.values()) output.add(value);
        return output;
    }
    
    private String getKey(String str) {
        char[] charArr = str.toCharArray();
        Arrays.sort(charArr);
        return new String(charArr);
    }
}

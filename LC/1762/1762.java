class Solution {
    public int[] findBuildings(int[] heights) {
        if (heights.length == 0) return heights;
        List<Integer> views = new ArrayList<>();
        views.add(heights.length-1);
        
        int maxHeight = heights[heights.length-1];
        for (int i = heights.length-2; i >= 0; i--) {
            if (heights[i] <= maxHeight) continue;
            views.add(i);
            maxHeight = heights[i];
        }
        
        Collections.reverse(views);
        return views.stream().mapToInt(i -> i).toArray();
    }
}
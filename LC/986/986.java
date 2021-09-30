class Solution {
    public int[][] intervalIntersection(int[][] firstList, int[][] secondList) {
        if (firstList.length == 0 || secondList.length == 0) {
            return (firstList.length == 0) ? firstList : secondList;
        }
        
        int firstInd = 0;
        int secondInd = 0;
        
        List<int[]> intersections = new ArrayList<>();
        
        while (firstInd < firstList.length && secondInd < secondList.length) {
            int firstStart = firstList[firstInd][0];
            int firstEnd = firstList[firstInd][1];
            
            int secondStart = secondList[secondInd][0];
            int secondEnd = secondList[secondInd][1];
            
            // Check if there's no overlap
            if (secondStart > firstEnd || firstStart > secondEnd) {
                if (secondStart > firstEnd) firstInd++;
                if (firstStart > secondEnd) secondInd++;
                continue;
            }
            
            // Found intersection, add to the result
            int[] intersection = new int[2];
            intersection[0] = Math.max(firstStart, secondStart);
            intersection[1] = Math.min(firstEnd, secondEnd);
            intersections.add(intersection);
            
            if (firstEnd == secondEnd) {
                firstInd++;
                secondInd++;
            } else if (firstEnd > secondEnd) {
                secondInd++;
            } else {
                firstInd++;
            }
        }
        
        int[][] results = new int[intersections.size()][];
        results = intersections.toArray(results);
        return results;
    }
}
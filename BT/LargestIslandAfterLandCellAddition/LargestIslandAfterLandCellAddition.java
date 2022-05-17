import java.util.*;

/*
rootId matrix => root id that each cell belongs to

*/
class Solution {
    public int solve(int[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) return 0;

        int m = matrix.length;
        int n = matrix[0].length;

        // Map rootId to land count
        Map<Integer, Integer> map = new HashMap<>();
        Queue<int[]> zeros = new LinkedList<>();
        int[][] rootMatrix = new int[m][n];

        // Find the start point
        int rootId = 1;
        int maxCount = 0;

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (matrix[r][c] == 1) {
                    matrix[r][c] = -1;
                    rootMatrix[r][c] = rootId;
                    int landCount = countLand(matrix, r, c, rootMatrix, rootId);
                    maxCount = Math.max(maxCount, landCount);
                    map.put(rootId, landCount);
                    rootId++;
                } else if (matrix[r][c] == 0) {
                    zeros.offer(new int[]{r, c});
                }
            }
        }

        int[][] coords = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        while (!zeros.isEmpty()) {
            int[] position = zeros.poll();
            int row = position[0],
                col = position[1];
            
            Set<Integer> visited = new HashSet<>();
            int count = 0;
            for (int[] coord: coords) {
                int r = row + coord[0],
                    c = col + coord[1];
                
                if (r < 0 || r >= m || c < 0 || c >= n || matrix[r][c] == 0)
                    continue;
                
                int id = rootMatrix[r][c];
                if (!visited.contains((id))) {
                    count += map.getOrDefault(id, 0);
                    visited.add(id);
                }
            }
            maxCount = Math.max(count+1, maxCount);
        }
        return maxCount;
    }

    private int countLand(int[][] matrix, int row, int col, int[][] rootMatrix, int rootId) {
        int count = 1;
        int m = matrix.length,
            n = matrix[0].length;
        int[][] coords = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{row, col});

        while (!queue.isEmpty()) {
            int[] position = queue.poll();

            for (int[] coord: coords) {
                int r = position[0] + coord[0],
                    c = position[1] + coord[1];
                
                if (r < 0 || r >= m || c < 0 || c >= n || matrix[r][c] <= 0)
                    continue;
                
                matrix[r][c] = -1;
                rootMatrix[r][c] = rootId;
                count++;
                queue.offer(new int[]{r, c});
            }
        }
        return count;
    }
}

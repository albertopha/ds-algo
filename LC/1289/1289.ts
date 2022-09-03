function minFallingPathSum(grid: number[][]): number {
    if (grid.length === 0 || grid[0].length === 0) return 0;
    
    let m = grid.length,
        n = grid[0].length;
    
    const addMinPaths = (minPaths, col, value) => {
        if (minPaths[0][1] >= value) {
            const tmpCol = minPaths[0][0];
            const tmpVal = minPaths[0][1];
            minPaths[0] = [col, value];
            minPaths[1] = [tmpCol, tmpVal];
        } else if (minPaths[1][1] > value) {
            minPaths[1] = [col, value];
        }
    }
    
    for (let row = 1; row < m; row++) {
        const minPaths = [
            [0, grid[row-1][0]], [1, grid[row-1][1]]
        ].sort((a, b) => a[1] - b[1]);
        
        for (let col = 2; col < n; col++) {
            addMinPaths(minPaths, col, grid[row-1][col]);
        }
        
        for (let col = 0; col < n; col++) {
            if (minPaths[0][0] !== col) grid[row][col] += minPaths[0][1];
            else grid[row][col] += minPaths[1][1];
        }
    }
    
    return Math.min(...grid[grid.length-1]);
};

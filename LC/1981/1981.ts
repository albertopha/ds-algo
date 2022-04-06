/*
[1,2,3]
[4,5,6]
[7,8,9]

[1]
[5,6,7]
[12,13,14]

[1,0,1]
                 1          2          3
[0,...,4900]
[]
                 
*/
function minimizeTheDifference(mat: number[][], target: number): number {
    const dp = new Array(mat.length).fill(null).map((row) => new Array(4900).fill(null));
    return dfs(mat, 0, target, 0, dp);
};

function dfs(mat: number[][], row: number, target: number, sum: number, dp: number[][]): number {
    if (row >= mat.length) return Math.abs(target-sum);
    
    if (dp[row][sum] !== null) return dp[row][sum];
    
    let smallestDiff = Number.MAX_SAFE_INTEGER;
    for (let col = 0; col < mat[0].length; col++) {
        smallestDiff = Math.min(smallestDiff, dfs(mat, row+1, target, sum+mat[row][col], dp));
    }
    dp[row][sum] = smallestDiff;
    return smallestDiff;
};

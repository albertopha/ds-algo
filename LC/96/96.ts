/**
3 =>                    1                       2                       3
                        |                      | \                      |
                       2,3                    1   3                    1,2
                       
   [1, 2, 3, 4, 5...]
   
   1 -> 1
   2 -> 2
   3 -> 3 = (2 + 1 + 2)
   4 -> 4 = (5 + (1+2) + (1+2) + )
*/
function numTrees(n: number): number {
  if (n <= 0) return 0;
  const dp = new Array(n+1).fill(1);
  dp[2] = 2;
  
  for (let nodes: number = 3; nodes <= n; nodes++) {
      let count: number = 0;
      for (let root: number = 1; root <= nodes; root++) {
          const lefts = root - 1;
          const rights = nodes - root;
          count += dp[lefts] * dp[rights];
      }
      dp[nodes] = count;
  }
  return Math.max(dp[n], 1);
};
/*
n = 1
[1]

n = 2
[1,2]

n = 3
=> (n = 1) + (n = 2)
[1,2,3]

n = 5
=> (n = 4) + (n = 3)
[1,2,3,5,8]
*/
class Solution {
    public int climbStairs(int n) {
        if (n <= 3) return n;
        
        int prev = 1;
        int next = 2;
        
        for (int i = 3; i <= n; i++) {
            int nextVal = prev + next;
            prev = next;
            next = nextVal;
        }
        
        return next;
    }
}

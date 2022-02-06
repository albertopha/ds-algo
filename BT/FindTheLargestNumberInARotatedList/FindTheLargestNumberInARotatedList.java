import java.util.*;

/*
[6,7,8,1,4]

[6,7,8,9,4]

[5,1,2,3,4]
[6,5,1,2,3,4]

[1,2,3,4,5]

*/
class Solution {
    public int solve(int[] arr) {
        if (arr.length == 0) return 0;
        int maxNum = arr[0];
        int l = 0, r = arr.length-1;
        while (l <= r) {
            int m = (l + r) / 2;
            maxNum = Math.max(maxNum, arr[m]);

            // Bottom half is sorted
            if (arr[l] < arr[m]) {
                l = m + 1;
            } else { // Top half is sorted
                // Record the highest
                maxNum = Math.max(maxNum, arr[r]);
                r = m - 1;
            }
        }
        return maxNum;
    }
}

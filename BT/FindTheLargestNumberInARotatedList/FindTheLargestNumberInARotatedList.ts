class Solution {
    solve(arr: Array<number>): number {
        if (arr.length === 0) return -1;

        let l = 0,
            r = arr.length-1;
        
        let maxInt = arr[0];
        while (l <= r) {
            const m = Math.floor((l+r)/2);

            if (arr[l] <= arr[m]) {
                maxInt = Math.max(arr[m], maxInt);
                l = m+1;
            } else {
                maxInt = Math.max(arr[r], maxInt);
                r = m-1;
            }
        }
        return maxInt
    }
}

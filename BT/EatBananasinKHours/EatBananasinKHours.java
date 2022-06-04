import java.util.*;

/*
[6,4,3]
k = 3
r = 6

[6,4,3]
k = 4
r = 4

13 / 4 = 4
13 / 5 = 3

[6,4,3]
k = 6

13 / 6 = 3

[6,2,1]
*/

class Solution {
    public int solve(int[] piles, int k) {
        if (piles.length == 0 || k < piles.length) return -1;

        int max = piles[0];
        int sum = 0;

        for (int i = 0; i < piles.length; i++) {
            max = Math.max(max, piles[i]);
            sum += piles[i];
        }

        int upperLimit = max;
        int bottomLimit = (int) Math.ceil(sum / (float) k);

        for (int r = bottomLimit; r <= upperLimit; r++) {
            int hours = getHours(piles, r);
            if (hours <= k) return r;
        }
        return -1;
    }

    private int getHours(int[] piles, int r) {
        int hours = 0;
        for (int i = 0; i < piles.length; i++) {
            hours += (int) Math.ceil(piles[i] / (float) r);
        }
        return hours;
    }
}

import java.util.*;

/*
8808800

9998800

534
*/

class Solution {
    public int solve(int n) {
        if (n == 0) return 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
            if (b[0] == a[0]) return a[1] - b[1];
            return b[0] - a[0];
        });

        List<Integer> nums = new ArrayList<>();

        int num = n;
        int index = 0;
        while (num > 0) {
            int lastDigit = num % 10;
            pq.offer(new int[]{lastDigit, index});
            nums.add(lastDigit);
            num /= 10;
            index++;
        }

        for (int i = nums.size()-1; i >= 0; i--) {
            int currNum = nums.get(i);
            while (!pq.isEmpty() && pq.peek()[1] >= i) pq.poll();
            if (pq.isEmpty()) break;
            if (currNum == 9 || pq.peek()[0] <= currNum) continue;
            nums.set(i, pq.peek()[0]);
            nums.set(pq.peek()[1], currNum);
            break;
        }

        int val = 0;
        for (int i = nums.size()-1; i >= 0; i--) {
            val *= 10;
            val += nums.get(i);
        }
        return val;
    }
}

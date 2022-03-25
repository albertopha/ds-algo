import java.util.*;

class Solution {
    public boolean solve(int[][] trips, int capacity) {
       if (trips.length == 0 || trips[0].length == 0 || capacity == 0) return false;

       Arrays.sort(trips, (trip1, trip2) -> {
           if (trip1[0] == trip2[0]) return trip1[1] - trip2[1];
           return trip1[0] - trip2[0];
       });

       int occupied = 0;
       Queue<int[]> pq = new PriorityQueue<>((prev, curr) -> prev[0] - curr[0]);
       
       for (int i = 0; i < trips.length; i++) {
           int pickupTime = trips[i][0];
           int dropOffTime = trips[i][1];
           int numOfCustomers = trips[i][2];

           while (!pq.isEmpty() && pq.peek()[0] <= pickupTime) {
               int[] curr = pq.poll();
               occupied -= curr[1];
           }

           occupied += numOfCustomers;
           pq.add(new int[]{dropOffTime, numOfCustomers});
           
           if (occupied > capacity) return false;
       }
       return true;
    }
}

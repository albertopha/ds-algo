import java.util.*;

/*
12 -> 360
1 -> 30

60 -> 360
1 -> 6

1 -> 60
1 -> 1/60 *  = 1/2 * 22 = 1/11
*/
class Solution {
    public int solve(int hour, int minutes) {
        double hourAngle = (hour % 12) * 30 + minutes * 0.5;
        int minutesAngle = minutes * 6;
        double angleBetween = Math.abs(hourAngle - minutesAngle);
        return (int) Math.min(360 - angleBetween, angleBetween);
    }
}

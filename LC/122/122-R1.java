/*
purchase: 4
sold: 7

[7,1,5,3,6,4]
           ^
           ^

purchase: 3
sold: 2

[1,2,3,4,5]
   ^
     ^
     

*/
class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length == 0) return 0;
        
        int purchased = 0;
        int sold = 0;
        
        for (int i = 0; i < prices.length; i++) {
            if (prices[purchased] < prices[i]) {
                sold += (prices[i] - prices[purchased]);
            }
            purchased = i;
        }
        return sold;
    }
}

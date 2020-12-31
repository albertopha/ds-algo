"""
============================================
Test cases:

[1, 2, 3, 0, 2]
       ^

 [0, 0, 0, 0, 0]
 [0, 0, 0, 0, 0]
 [0, 0, 0, 0, 0]
 [0, 0, 0, 0, 0]
 [0, 0, 0, 0, 0]


                        start
                      /        \
        (day 1)      -1          0
                    /  \       /   \
        (day 2)   1    -1     -2    0
                 / \   / \   / \   / \
        (day 3) 

[48,12,60,93,97,42,25,64,17,56,85,93,9,48,52,42,58,85,81,84,69,36,1,54,23,15,72,15,11,94]
============================================
Brute force (TLE):
1. We have 4 choices:
    buy, skip buy, sell, skip sell

2. Recursively call 4 choices with one caveat:
    if stock is sold, skip one extra day (ie. day + 2)
    to count for the cooldown period.

Tim O(2^N) each time, we have two choices (either buy/skip or sell/skip)
Space: O(N) for recursion stack
============================================
Optimal solution:

============================================
"""
class Solution(object):
    def maxProfit(self, prices):
        """ 
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        return self.optimal(prices)
        # return self.bruteForce(prices, 0, False)
    
    def bruteForce(self, prices, day, is_bought):
        if day >= len(prices):
            return 0
        
        if is_bought:
            return max(prices[day] + self.bruteForce(prices, day + 2, not is_bought),
                    self.bruteForce(prices, day + 1, is_bought))
        
        return max(-prices[day] + self.bruteForce(prices, day + 1, not is_bought),
                  self.bruteForce(prices, day + 1, is_bought))
    
    def optimal(self, prices):
        # Consists of three states (no_stock, bought, sold)
        no_stock = [0 for _ in range(len(prices))]
        bought = [0 for _ in range(len(prices))]
        sold = [0 for _ in range(len(prices))]
        bought[0] = -prices[0]
        
        for day in range(1, len(prices)):
            # no_stock --> either we just sold the stock and in a cooldown state
            # or we are skipping a day instead of buying the new stock
            no_stock[day] = max(sold[day - 1], no_stock[day - 1])
            
            # bought --> we skipped to buy the stock last day and buy it on the current day
            # or we already bought the stock and skip to sell it
            bought[day] = max(no_stock[day - 1] - prices[day], bought[day - 1])
            
            # sold --> we sell the stock we bought last time
            sold[day] = bought[day - 1] + prices[day]
        
        return max(no_stock[-1], bought[-1], sold[-1])
e

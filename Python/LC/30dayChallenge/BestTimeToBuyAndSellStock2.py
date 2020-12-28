from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            print('prices[i] -> ', prices[i])
            print('prices[i+1] -> ', prices[i+1])
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
                print('profit -> ', profit)
        return profit
        # return self.bruteForce(prices, 0, 0)

    # def bruteForce(self, prices: List[int], start: int, currentProfit: int) -> int:
    #     maxProfit = 0
    #     if start >= len(prices):
    #         return maxProfit
    #
    #     for i in range(start, len(prices) - 1):
    #         buy = prices[i]
    #
    #         for s_i in range(i, len(prices)):
    #
    #
    #     return maxProfit


if __name__ == '__main__':
    S = Solution()
    print(S.maxProfit([7, 1, 5, 3, 6, 4]))
    print(S.maxProfit([1, 2, 10, 2]))


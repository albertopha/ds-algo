function maxProfit(prices: number[]): number {
    if (!prices.length) return 0;
    
    let maxProfit = 0;
    let l = 0;
    
    for (let r = 0; r < prices.length; r++) {
        if (prices[r] < prices[l]) l = r;
        maxProfit = Math.max(prices[r]-prices[l], maxProfit);
    }
    
    return maxProfit;
};

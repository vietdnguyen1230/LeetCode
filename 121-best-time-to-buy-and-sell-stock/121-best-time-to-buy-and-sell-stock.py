class Solution:
    def maxProfit(self, prices: List[int]) -> int:
# set two pointers
        l, r = 0, 0
        maxProfit = 0
# while within range
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
# move the pointers
            else:
                l = r
            r += 1
        
        return maxProfit

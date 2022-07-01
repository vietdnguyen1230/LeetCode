class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0 
        res = 0
        
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                res = max(res, profit)
            else:
                l = r
            r += 1
        
        return res
    
    

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            buy_price = prices[i]
            for j in range(i+1, len(prices)):
                sell_price = prices[j]
                res = max(res, sell_price-buy_price)
        return res
        
            

            
            
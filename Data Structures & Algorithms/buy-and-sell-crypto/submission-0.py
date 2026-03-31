class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyRate =prices[0]
        maxProfit = 0
        for rate in prices[1:]:
            if rate<buyRate:
                buyRate=rate
            maxProfit = max(maxProfit,rate-buyRate)
        return maxProfit

        
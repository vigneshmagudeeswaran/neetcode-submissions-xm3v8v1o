class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """so here whatI need to do is initially my profit is going to
        be a 0 so ai m going to initialize the variable profit with value zer0
        then
            I am going to considervery first day as my buying day
            the I am going to start thefor loop in ther range of pricess
            so based on the index i can consider it as the selling price or buying price baced on
            whether it is lower then previous buying price or it's giving higher profits
            """
        profit = 0

        buy=prices[0]
        for i in range(len(prices)):
            profit= max(profit,prices[i]-buy)
            buy=min(buy,prices[i])
        return profit




        
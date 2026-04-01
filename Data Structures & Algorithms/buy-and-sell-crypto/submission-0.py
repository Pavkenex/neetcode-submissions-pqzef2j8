class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #brute force

        maxProfit=0
        l,r = 0, 1

        for i in range(len(prices)):
            for j in range(i, len(prices)):
                if(prices[i]>prices[j]):
                    continue
                if(prices[j]-prices[i]> maxProfit):
                    maxProfit = prices[j]-prices[i]

            
        return maxProfit
        
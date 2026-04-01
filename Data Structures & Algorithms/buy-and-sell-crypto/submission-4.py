class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #brute force
        maxProfit=0
        l,r = 0, 1
        while r< len(prices):
            if(prices[l]>prices[r]):
                l=r
                r+=1
                continue
            maxProfit = max(maxProfit, prices[r]- prices[l])
            r+=1
        return maxProfit
        
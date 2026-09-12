class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        lmax = [prices[-1]]*n
        for i in range(n-2,-1,-1):
            lmax[i] = max(lmax[i+1],prices[i])
        ans = 0
        for i in range(n):
            ans = max(ans,abs(lmax[i]-prices[i]))
        return ans
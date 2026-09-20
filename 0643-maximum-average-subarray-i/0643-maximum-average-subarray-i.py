class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        i = 0
        j = i+k
        n = len(nums)
        sm = sum(nums[:k])
        mx = sm
        for i in range(k,n):
            sm+=nums[i]
            sm-=nums[i-k]
            mx = max(sm,mx)
        return mx/k
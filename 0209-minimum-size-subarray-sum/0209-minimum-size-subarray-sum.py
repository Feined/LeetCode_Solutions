class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        minLen = float('inf')
        n = len(nums)
        sm = 0
        l = 0
        for r in range(n):
            sm+=nums[r]
            while sm>=target:
                sm-=nums[l]
                minLen = min(minLen,r-l+1)
                l+=1
        return minLen if minLen!=float('inf') else 0


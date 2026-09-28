class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        sm = 0
        mx = float('-inf')
        if len(nums)<=1:
            return nums[0]
        for i in range(len(nums)):
            sm+=nums[i]
            if sm>mx:
                mx = sm
            if sm<0:
                sm = 0

        return mx
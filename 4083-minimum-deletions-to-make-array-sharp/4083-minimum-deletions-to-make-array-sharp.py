class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        i = 0
        ans = 0
        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                ans+=1
            i+=1
        return ans
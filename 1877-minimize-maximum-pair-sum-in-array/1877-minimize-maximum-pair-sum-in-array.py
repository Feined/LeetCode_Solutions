class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        i = 0
        j = n-1
        res = 0
        while i<j:
            sm = nums[i]+nums[j]
            res = max(res,sm)
            i +=1
            j-=1
        return res
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        sm = 0
        n = len(nums)
        for i in range(n):
            for j in range(n):
                rem = nums[i:j+1]
                sm+=(len(set(rem)))**2
        return sm
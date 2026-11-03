class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mxVal = max(nums)
        cst = 0
        for i in nums:
            cst+=(abs(i-mxVal))
        return (cst)
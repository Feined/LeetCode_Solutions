class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = []
        for i in nums:
            n.append(i*i)
        # print(n)
        n.sort()
        ln = len(n)
        small = sum(n[:ln//2])
        large = sum(n[ln//2:]) 
        return large-small
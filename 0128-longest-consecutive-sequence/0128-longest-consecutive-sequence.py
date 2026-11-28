class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num = set(nums)
        ln = 0
        for i in num:
            if i-1 not in num:
                curr = i
                mx = 1
                while curr+1 in num:
                    curr = curr+1
                    mx+=1
                ln = max(ln,mx)
        return ln
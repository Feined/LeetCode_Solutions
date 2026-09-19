import itertools
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        for p in itertools.permutations(nums,len(nums)):
            res.append(list(p))
        return res
        
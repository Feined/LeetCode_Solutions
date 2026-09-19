class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = set()
        for p in itertools.permutations(nums,len(nums)):
            res.add(p)
        return list(res)
        
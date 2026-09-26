class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        for i in nums[:]:
            nums.append(int(str(i)[:][::-1]))
        return len(set(nums))
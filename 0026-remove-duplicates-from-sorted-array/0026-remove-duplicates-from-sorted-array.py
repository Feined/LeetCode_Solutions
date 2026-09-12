class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        st = 1 # Points to unique elements
        for i in range(1,len(nums)): # First Element always unique
            if nums[i]!=nums[i-1]:
                nums[st]=nums[i]
                st+=1
        return st

            
        
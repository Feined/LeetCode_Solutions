class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums.sort()
        
        n = len(nums)
        
        o = 0
        t = n-1

        curr = 0

        while curr<=t:
            if nums[curr]==0:
                nums[curr],nums[o]=nums[o],nums[curr]
                curr+=1
                o+=1
            elif nums[curr]==2:
                nums[curr],nums[t]=nums[t],nums[curr]
                t-=1
            else:
                curr+=1
        
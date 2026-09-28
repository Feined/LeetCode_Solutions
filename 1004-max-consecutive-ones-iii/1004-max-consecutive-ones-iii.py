class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l = 0
        mx = 0
        zc = 0 
        n = len(nums)
        ''' Approach -1 
        # Iterating in the array
        for r in range(n):
            # Calculate the no. of zeroes
            if nums[r]==0:
                zc+=1
            # Shrink the window when count>k
            while zc>k:
                if nums[l]==0:
                    zc-=1
                l+=1
            # Calculate the max
            mx = max(mx,r-l+1)
        return mx
        '''
        for r in range(n):
            # Calculate the no. of zeroes
            if nums[r]==0:
                zc+=1
            # Shrink the window when count>k
            if zc>k:
                if nums[l]==0:
                    zc-=1
                l+=1
            # Calculate the max
            mx = max(mx,r-l+1)
        return mx
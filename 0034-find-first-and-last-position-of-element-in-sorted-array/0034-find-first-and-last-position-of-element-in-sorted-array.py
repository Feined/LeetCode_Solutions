class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        # Approach - 1
        '''
        cnt = []
        n= len(nums)
        if target in nums:
            x = nums.index(target)
            cnt.append(x)
        rev = nums[::-1]
        # print(rev)
        if target in rev:
            y = rev.index(target)
            cnt.append(n-y-1)
        if len(cnt)==0: return [-1,-1]
        else: return cnt
        '''
        # Approach - 2
        left = 0
        right = len(nums)-1
        lft = -1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                lft = mid
                right = mid-1
            elif nums[mid]<target:
                left = mid+1
            else:
                right = mid-1
        left = 0
        right = len(nums)-1
        rgt = -1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                rgt = mid
                left = mid+1
            elif nums[mid]<target:
                left = mid+1
            else:
                right = mid-1
        return [lft,rgt]
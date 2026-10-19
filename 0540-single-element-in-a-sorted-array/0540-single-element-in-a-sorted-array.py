class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # Approach 1 - O(N),O(1)
        '''
        if len(nums)<2:
            return nums[0]
        i = 1
        while i<len(nums):
            if nums[i]==nums[i-1]:
                i+=2
            else:
                return nums[i-1]
        return nums[-1]
        '''

        # Approach 2 - O(logN)
        low,high = 0,len(nums)-1
        while low<high:
            mid = (low+high)//2
            if mid%2==1:
                mid-=1
            if nums[mid]==nums[mid+1]:
                low = mid+2
            else:
                high = mid
        return nums[low]
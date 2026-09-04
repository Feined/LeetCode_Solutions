class Solution:
    def firstStableIndex(self, nums1: list[int], k: int) -> int:

        # Approach - 1
        sm = []
        for i in range(len(nums1)):
            if max(nums1[0:i+1])-min(nums1[i:])<=k:
                return i
        return -1
        
        # Approach - 2

        n = len(nums1)
        pref = [0]*n
        suff = [0]*n

        pref[0] = nums1[0]
        suff[n-1] = nums1[n-1]
        for i in range(1,n):
            pref[i] = max(pref[i-1],nums1[i])
        for i in range(n-2,-1,-1):
            suff[i] = min(suff[i+1],nums[i])
        for i in range(n):
            if pref[i]-suff[i]<=k:
                return i
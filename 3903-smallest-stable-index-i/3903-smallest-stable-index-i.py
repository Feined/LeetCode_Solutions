class Solution:
    def firstStableIndex(self, nums1: list[int], k: int) -> int:

        # Approach - 1
        sm = []
        for i in range(len(nums1)):
            if max(nums1[0:i+1])-min(nums1[i:])<=k:
                return i
        return -1
        
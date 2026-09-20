from collections import Counter
class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        sm = sum(nums[:k])
        st = set(nums[:k])
        mx = sm if len(st)==k else 0
        freq = Counter(nums[:k])
        for i in range(k,n):
            sm+=nums[i]
            sm-=nums[i-k]
            freq[nums[i-k]]-=1
            if freq[nums[i-k]]==0:
                del freq[nums[i-k]]
            freq[nums[i]]+=1
            if len(freq) == k:
                mx = max(mx, sm)
        return mx
from math import gcd
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        p = []
        n  =len(nums)
        mx = 0
        for i in range(n):
            mx = max(mx,nums[i])
            p.append(gcd(mx,nums[i]))
        
        p.sort()
        i = 0
        j = len(p)-1
        res = 0
        while i<j:
            res+=gcd(p[i],p[j])
            i+=1
            j-=1
        return res
        
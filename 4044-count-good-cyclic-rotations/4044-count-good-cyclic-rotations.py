class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        n = len(nums)
        total = sum(nums)
        fhalf = sum(nums[:n//2])
        res = 0
        for i in range(n):
            if 2*fhalf>total:
                res+=1
            fhalf-=nums[i]
            fhalf+=nums[(i+n//2)%n]
            
        return res


        
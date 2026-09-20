class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        c = 0
        mx = 0
        for i in nums:
            if i==1:
                c+=1
                if c>mx:
                    mx = c
            else:
                c = 0
        return mx
        
class Solution:
    def jump(self, nums: List[int]) -> int:
        man = 0
        jump = 0
        curr=0
        for i in range(len(nums)-1):
            man = max(man,i+nums[i])
            if i==curr:
                jump+=1
                curr = man
        return jump
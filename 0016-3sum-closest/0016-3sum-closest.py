class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        closest = nums[0]+nums[1]+nums[2]
        for i in range(n-2):
            l = i+1
            r = n-1
            while l<r:
                tot = nums[i]+nums[l]+nums[r]
                if abs(target-tot)<abs(target-closest):
                    closest = tot
                if tot==target:
                    return target
                elif tot<target:
                    l+=1
                else:
                    r-=1
        return closest

            
        
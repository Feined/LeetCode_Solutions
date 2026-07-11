class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Approach 1 - Brute Force
        '''
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return []
        '''
        # Approach 2 - hashmap
        
        hashmap = {}
        n = len(nums)
        for i in range(n):
            comp = target - nums[i]
            if comp in hashmap:
                return [hashmap[comp],i]
            else:
                hashmap[nums[i]]=i
        return []
        
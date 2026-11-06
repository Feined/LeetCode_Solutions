class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        cnt = 0
        ans = 0
        for i in range(len(nums)):
            if cnt==0:
                ans = nums[i]
            if nums[i]==ans:
                cnt+=1
            else:
                cnt-=1
        return ans
        '''
        return max(set(nums), key = nums.count)
        '''
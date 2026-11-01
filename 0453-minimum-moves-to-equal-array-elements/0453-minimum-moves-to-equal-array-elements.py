class Solution:
    def minMoves(self, nums: list[int]) -> int:
        if min(nums)==max(nums):
            return 0
        else:

            # Brute Force
            '''
            cnt = 0
            while min(nums)!=max(nums):
                mxInd = nums.index(max(nums))
                k = len(nums)-1
                for i in range(len(nums)):
                    if i!=mxInd and k>0:
                        nums[i]+=1
                        k-=1
                cnt+=1
            return cnt
            '''

            return sum(nums)-(len(nums))*min(nums)

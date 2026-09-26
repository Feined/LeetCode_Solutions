class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        pproduct = [1]*(n+1)
        sproduct = [1]*(n+1)
        for i in range(1,n+1):
            pproduct[i]=pproduct[i-1]*nums[i-1]
        for i in range(n-1,-1,-1):
            sproduct[i]=sproduct[i+1]*nums[i]       
        l = []
        for i in range(n):
            l.append(pproduct[i]*sproduct[i+1])
        return l

        # return pproduct,  sproduct
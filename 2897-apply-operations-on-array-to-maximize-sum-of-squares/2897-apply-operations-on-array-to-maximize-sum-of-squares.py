class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        m = 10**9+7
        res = 0
        bits = [0]*32
        for i in nums:
            for j in range(32):
                if i&(1<<j):
                    bits[j]+=1
        while k>0:
            curr = 0
            for i in range(0,31):
                if bits[i]>0:
                    bits[i]-=1
                    curr = (curr|(1<<i))
            res+=(curr*curr)%m
            k-=1
        return res%m
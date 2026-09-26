class Solution:
    def trap(self, l: List[int]) -> int:
        n = len(l)
        lm,rm = [0]*n,[0]*n
       
        lm[0]=l[0]
        rm[n-1]=l[n-1]
        for i in range(1,n):
            lm[i]=max(lm[i-1],l[i])
        for i in range(n-2,-1,-1):
            rm[i]=max(rm[i+1],l[i])
        tw = 0
        for i in range(n):
            tw+=min(lm[i],rm[i])-l[i]
        return tw
        
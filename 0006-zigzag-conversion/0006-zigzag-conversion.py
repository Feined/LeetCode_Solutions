class Solution:
    def convert(self, s: str, n: int) -> str:
        if n==1: return s
        res = ['']*n
        i = 0
        cnt = 1
        for ch in s:
            res[i]+=(ch)
            if i==0:
                cnt = 1
            elif i==n-1:
                cnt = -1
            i+=cnt
        return ''.join(res)
class Solution:
    def romanToInt(self, s: str) -> int:
        v = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        t = 0
        for i in range(len(s)-1):
            if v[s[i]]<v[s[i+1]]:
                t-=v[s[i]]
            else:
                t+=v[s[i]]
        t+=v[s[-1]]
        return t
        
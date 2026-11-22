class Solution:
    def checkString(self, s: str) -> bool:
        n = len(s)
        acount = s.count('a')
        for i in range(n):
            if s[i]=='a': acount-=1
            elif s[i]!='a' and acount>0: return False
        return True
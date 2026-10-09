class Solution:
    def minInsertions(self, s: str) -> int:
        cnt = 0
        res = 0
        i = 0
        n = len(s)
        while i<n:
            if s[i]=='(':
                cnt+=1
                i+=1
            elif s[i]==')':
                if cnt>0:
                    cnt-=1
                else:
                    res+=1 # If an Open brackent is not present befor ")"
                if i<n-1 and s[i+1]==')':
                    i+=2
                else:
                    res+=1 # If an closing bracket is not present after ")"
                    i+=1
        if cnt!=0: # If any extra Opening bracket remaining
            res+=(2*cnt)
        return res
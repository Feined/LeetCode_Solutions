class Solution:
    def minChanges(self, s: str) -> int:
        curr = s[0]  # Maintaining a previous 
        n = len(s)
        cnt = 0
        change = 0
        for i in range(n):
            if s[i]==curr:
                cnt+=1
                continue
            if cnt%2==0:
                cnt=1
            else:
                change+=1
                cnt = 0
            curr = s[i]
        return change
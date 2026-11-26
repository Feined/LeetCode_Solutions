class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n<10: return False
        elif n==10: return True
        
        cnt = 0
        for i in range(10,-1,-1):
            if i<=n:
                cnt+=1
            n = n-i
        return True if cnt%2!=0 else False
        print(cnt)
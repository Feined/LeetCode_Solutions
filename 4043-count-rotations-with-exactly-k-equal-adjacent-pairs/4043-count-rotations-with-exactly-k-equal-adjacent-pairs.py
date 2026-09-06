class Solution:
    def countRotations(self, s: str, k: int) -> int:
        res = 0
        for shift in range(len(s)):
            rem = s[shift:]+s[:shift]
            c = 0
            for j in range(1,len(rem)):
                if rem[j]==rem[j-1]:
                    c+=1
            if c==k:
                res+=1

        return res

            
        
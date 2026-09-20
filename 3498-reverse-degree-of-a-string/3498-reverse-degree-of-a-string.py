class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            degree = ord('a')-ord(s[i])+26
            res+=degree*(i+1)
        return res
        
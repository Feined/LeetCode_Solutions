class Solution:
    def isPalindromic(self, s: str) -> bool:
        b = ''
        for i in s:
            bn = bin(ord(i))[2:]
            l = 8-len(bn)
            b+='0'*l+bn
        return b==b[::-1]
        
        
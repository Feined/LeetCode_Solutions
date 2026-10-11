class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(c**0.5)
        while a<=b:
            sm = (a*a)+(b*b)
            if sm==c:
                return True
            elif sm>c:
                b-=1
            else:
                a+=1
        return False
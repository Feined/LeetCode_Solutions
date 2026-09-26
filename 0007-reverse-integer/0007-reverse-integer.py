class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            rev = (-1)*(int(str(x)[1:][::-1]))
        else:
            rev = int(str(x)[:][::-1])
        if rev<-(pow(2,31)) or rev>(pow(2,31)-1):
            return 0
        else:
            return rev
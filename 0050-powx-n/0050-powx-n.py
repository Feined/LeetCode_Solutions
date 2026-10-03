class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Approach -1
        # return pow(x,n)%(10**9+7)

        # Approach - 2 : Recursion

        if n==0:
            return 1
        if n<0:
            return 1/self.myPow(x,-n)
        small = self.myPow(x,n//2)
        if n % 2 == 0:
            return small * small
        else:
            return small * small * x
        
        
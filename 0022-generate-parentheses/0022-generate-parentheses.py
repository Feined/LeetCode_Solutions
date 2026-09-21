class Solution:
    def solve(self,l,n,cc,co,s):
        if len(s)==2*n:
            l.append(s)
        if co<n:
            self.solve(l,n,cc,co+1,s+'(')
        if cc<co:
            self.solve(l,n,cc+1,co,s+')')
    def generateParenthesis(self, n: int) -> list[str]:
        l = []
        self.solve(l,n,0,0,'')
        return l
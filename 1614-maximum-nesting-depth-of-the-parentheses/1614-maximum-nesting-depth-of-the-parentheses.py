class Solution:
    def maxDepth(self, s: str) -> int:
        rb = ob = 0
        mx = float('-inf')
        for ch in s:
            if ch=='(':
                ob+=1
            elif ch==')':
                rb+=1
            
            mx = max(mx,ob-rb)
        return mx
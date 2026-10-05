class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        lst = []
        n = len(s)
        score = 0
        for ch in range(n):
            if s[ch]=='(':
                lst.append(score)
                score = 0
            else:
                if ch>0 and s[ch-1]=='(':
                    score = lst[-1]+1   
                else:
                    score = lst[-1] + 2*score
                lst.pop()
        return score
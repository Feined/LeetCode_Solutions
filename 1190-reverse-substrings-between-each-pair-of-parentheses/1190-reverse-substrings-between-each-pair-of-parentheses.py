class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        res = []
        l = []
        for i in s:
            if i=='(':
                l.append(len(res))
            elif i==')':
                top = l.pop()
                res[top:]=(res[top:][::-1])
            else:
                res.append(i)
        return ''.join(res)
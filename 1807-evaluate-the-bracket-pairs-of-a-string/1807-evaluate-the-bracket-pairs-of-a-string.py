from collections import Counter
class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        i = 0
        n = len(s)
        isbracketopen = False
        result = []
        hm = {}
        for key,val in knowledge:
            hm[key] = val
        temp = ''
        while i<n:
            if s[i]=='(':
                isbracketopen = True
                temp = ''
            elif s[i]==')':
                isbracketopen = False
                result.append(hm.get(temp,"?"))
            elif isbracketopen:
                temp+=s[i]
            else:
                result.append(s[i])
            i+=1
        return "".join(result)


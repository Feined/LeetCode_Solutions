class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ss = sorted(strs)
        ans = ''
        fst = ss[0]
        lst = ss[-1]
        for i in range(min(len(fst),len(lst))):
            if fst[i]==lst[i]:
                ans+=fst[i]
            else:
                return ans
        return ans
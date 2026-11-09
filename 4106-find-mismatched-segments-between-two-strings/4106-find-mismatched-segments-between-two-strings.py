class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        res = []
        uncommon1 = ''
        uncommon2 = ''
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                uncommon1+=s1[i]
                uncommon2+=s2[i]
            else:
                if uncommon1:
                    res.append([uncommon1,uncommon2])
                    uncommon1 = ''
                    uncommon2 = ''
        if uncommon1:
            res.append([uncommon1,uncommon2])
        return res
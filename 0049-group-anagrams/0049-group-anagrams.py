class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hm = {}
        for i in strs:
            key = ''.join(sorted(i))
            if key not in hm:
                hm[key] = []
            hm[key].append(i)
        return sorted(hm.values())
        

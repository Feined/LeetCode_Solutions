class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        copy = sorted(set(arr))
        st = {}
        for ind,val in enumerate(copy):
            if val not in st:
                st[val] = ind+1
        return [st[val] for val in arr]
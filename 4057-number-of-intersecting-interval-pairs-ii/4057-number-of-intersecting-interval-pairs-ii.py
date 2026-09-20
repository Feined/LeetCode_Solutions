class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        res = 0
        st = sorted(x[0] for x in intervals)
        end = sorted(x[1] for x in intervals)
        j = 0
        n = len(intervals)
        total = n*(n-1)//2
        for s in st:
            while j<n and end[j]<s:
                j+=1
            res+=j
        return total-res
class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        res = 0
        n = len(intervals)
        for i in range(n):
            for j in range(i+1,n):
                if max(intervals[i][0], intervals[j][0]) <= min(intervals[i][1], intervals[j][1]):
                    res+=1
        return res

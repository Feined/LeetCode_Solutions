import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        c = Counter(nums)
        heap = []
        for key,val in c.items():
            heapq.heappush(heap,(-val,key))
        print(heap)
        res = []
        while k>0:
            val,temp = heapq.heappop(heap)
            res.append(temp)
            k-=1
        return res
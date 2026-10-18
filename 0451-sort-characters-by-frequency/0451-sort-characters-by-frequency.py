from collections import Counter
import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        heap = []
        for key,val in c.items():
            heapq.heappush(heap,(-val,key))
        # print(heap)
        res = ''
        for i in range(len(heap)):
            val,temp = heapq.heappop(heap)
            res+=temp*(-val)
        # print(res)
        return res
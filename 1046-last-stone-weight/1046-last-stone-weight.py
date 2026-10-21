import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = []
        for i in stones:
            heapq.heappush(heap,-i)
        while len(heap)>=2:
            frst = heapq.heappop(heap)
            scnd = heapq.heappop(heap)
            if frst==scnd:
                continue
            else:
                heapq.heappush(heap,-(abs(frst-scnd)))
        sm = 0
        for i in heap:
            sm+=(-i)
        return sm

import heapq
import math
class Solution:
    def minStoneSum(self, nums: list[int], k: int) -> int:
        heap= []
        sm = 0
        for i in nums:
            heapq.heappush(heap,-i)
        while k>0:
            heapq.heappush(heap,((heapq.heappop(heap))//2))
            k-=1
        for i in heap:
            sm+=(-i)
        return sm
        

import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # Approach 1 - 0(NlogN)
        '''
        nums.sort(reverse=True)
        return nums[k-1]
        '''

        # Approach 2 - O(nlogn)
        # MAx Heap
        '''
        heap = []
        for i in nums:
            heapq.heappush(heap,-i)
        while k>0:
            temp = -heapq.heappop(heap)
            k-=1
            if k==0:
                return temp
        ''' 
        # Approach 3 - 0(NlogK)
        heap = []
        for i in nums:
            if len(heap)<k:
                heapq.heappush(heap,i)
            elif i>heap[0]:
                heapq.heapreplace(heap,i)
        return heap[0]
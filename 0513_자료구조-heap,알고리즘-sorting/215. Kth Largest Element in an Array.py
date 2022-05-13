from heapq import heapify, heappushpop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # sol1 정렬
        return sorted(nums, reverse=True)[k-1]

        # sol2 크기가 k인 min-heap사용
        heap = nums[:k]
        heapify(heap)
        for n in nums[k:]:
            heappushpop(heap, n)
        return heap[0]

        # sol3 min-heap
        minheap = []
        for num in nums:
            heappush(minheap, num)
            if len(minheap) > k:
                heappop(minheap)
        return minheap[0]

        # sol4 max-heap
        maxheap = [-x for x in nums]
        heapify(maxheap)
        for _ in range(k-1):
            heappop(maxheap)
        return -maxheap[0]
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        heap = []
        for stone in stones:
            heapq.heappush(heap,-stone)
        while len(heap)>1:
            prev = abs(heapq.heappop(heap))
            curr = abs(heapq.heappop(heap))
            if prev != curr:
                heapq.heappush(heap,-abs(prev-curr))
        return abs(heap[0]) if heap else 0
        
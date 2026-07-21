class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq

        hm = {}
        for num in nums:
            hm[num] = hm.get(num,0) + 1
        heap = []
        for key,val in hm.items():
            heapq.heappush(heap,(-val,key))
        # print(heap)
        res = []
        for i in range(k):
            val,key = heapq.heappop(heap)
            res.append(key)
        return res

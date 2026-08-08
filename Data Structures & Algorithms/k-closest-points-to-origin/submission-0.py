class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        heap = []
        for i,point in enumerate(points):
            dist = math.sqrt(point[0]**2+point[1]**2)
            heapq.heappush(heap,(dist,point))
        res = []
        while k > 0:
            temp = heapq.heappop(heap)
            res.append(temp[1])
            k -= 1
        return res
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def valid(k,h2):
            for x in piles:
                h2 -= math.ceil(x/k)
            return True if h2 >= 0 else False

        i = 1
        j = max(piles)
        mini = float('inf')
        while i<=j:
            mid = i + (j-i)//2
            if valid(mid,h):
                mini = min(mini,mid)
                j = mid-1
            else:
                i = mid + 1
        return mini
        
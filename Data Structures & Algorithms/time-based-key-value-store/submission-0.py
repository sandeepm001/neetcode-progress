     
class TimeMap:

    def __init__(self):
        from collections import defaultdict
        self.hm = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hm[key].append((value,timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        arr = self.hm[key]

        i,j = 0, len(arr)-1
        res = ""
        while i <= j:
            mid = (i+j)//2
            if arr[mid][1] <= timestamp:
                res = arr[mid][0]
                i = mid + 1
            else:
                j = mid - 1
        return res
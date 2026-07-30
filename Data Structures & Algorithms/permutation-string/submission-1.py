class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target= Counter(s1)
        n = len(s1)
        m = len(s2)
        if n>m:
            return False
        window = Counter(s2[:n])
        if target==window:
            return True
        l = 0
        for i in range(n,m):
            window[s2[i]] += 1
            window[s2[l]] -= 1
            l += 1
            if window [s2[i-n]]==0:
                del window[s2[i-n]]
            if target==window:
                return True
            
        return False
            


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target= Counter(s1)
        n = len(s1)
        m = len(s2)
        if n>m:
            return False
        if target==Counter(s2[:n]):
            return True
        
        for i in range(m-n+1):
            if target==Counter(s2[i:i+n]):
                return True
        return False
            


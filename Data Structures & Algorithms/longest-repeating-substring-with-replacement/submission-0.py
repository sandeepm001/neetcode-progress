class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = defaultdict(int)
        maxi = 0
        j = 0
        max_freq =  0
        for i in range(len(s)):
            hm[s[i]] += 1
            max_freq = max(max_freq,hm[s[i]])
            while (i-j+1)-max_freq > k:
                hm[s[j]] -= 1
                j += 1
            maxi = max(maxi,i-j+1)            
        return maxi
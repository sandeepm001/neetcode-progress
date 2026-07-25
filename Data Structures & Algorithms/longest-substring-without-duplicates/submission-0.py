class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        hm = defaultdict(int)
        n = len(s)
        j = 0
        maxi = 0
        for i in range(n):
            while s[i] in hm:
                # print(s[i])
                del hm[s[j]]
                j += 1
            hm[s[i]] += 1
            maxi = max(maxi,i-j+1)
        return maxi

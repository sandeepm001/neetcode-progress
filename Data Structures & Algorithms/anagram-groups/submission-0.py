class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        hm = defaultdict(list)
        for x in strs:
            p = ''.join(sorted(x))
            hm[p].append(x)
        res = [val for _,val in hm.items()]
        return res
            
        

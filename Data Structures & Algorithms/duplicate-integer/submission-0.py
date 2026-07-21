class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = Counter(nums)
        for key,val in hm.items():
            if val > 1:
                return True
        return False
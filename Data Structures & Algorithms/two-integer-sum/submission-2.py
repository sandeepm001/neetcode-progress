class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i,num in enumerate(nums):
            x = target - num

            if x in hm:
                return [hm[x],i]
            hm[num] = i

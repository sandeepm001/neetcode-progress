class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
         
        slow = nums[0]
        fast = nums[nums[0]]

        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]
        #ONce we find the cycle we go back to start to get the duplicate val

        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow

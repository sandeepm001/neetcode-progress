class Solution:
    def findMin(self, nums: List[int]) -> int:

        i , j = 0,len(nums)-1
        mini = nums[i]
        while i <= j:
            mid = (i+j)//2
            if nums[i]<=nums[mid]:
                mini = min(nums[i],mini)
                i = mid + 1
            else:
                mini = min(nums[mid],mini)
                j = mid - 1
        return mini
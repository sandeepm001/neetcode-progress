class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [0]*n
        prev = 1
        for i in range(n):
            dp[i] = prev
            prev = dp[i]*nums[i]
        print(dp)
        suff = 1
        for i in range(n-1,-1,-1):
            dp[i] *= suff
            suff *= nums[i]
        return dp
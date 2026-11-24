class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * (n+1)
        def cal_rob(i):
            if i == n-1:
                return nums[i]
            if i >= n:
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(nums[i] + cal_rob(i+2), cal_rob(i+1))
            return memo[i]
        return cal_rob(0)
        
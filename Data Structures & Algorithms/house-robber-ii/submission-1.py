class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)-1
        firstCase = nums[1:]
        SecondCase = nums[:-1]
        if len(nums) == 1:
            return nums[0]
        return max(self.cal_rob(firstCase,0, [-1] * (n + 1)),
        self.cal_rob(SecondCase,0, [-1] * (n + 1)))

    def cal_rob(self, nums, i, memo):
        if i == len(nums)-1:
            return nums[i]
        if i >= len(nums):
            return 0
        if memo[i] != -1:
            return memo[i]
        memo[i] = max(nums[i] + self.cal_rob(nums,i+2, memo), 
        self.cal_rob(nums,i+1,memo))
        return memo[i]
            
        
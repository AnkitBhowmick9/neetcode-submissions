class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n+1)
 
        def count_steps(n):
            if n <= 1:
                return 1
            if memo[n] != -1:
                return memo[n]
            memo[n] = count_steps(n-1) + count_steps(n-2)
            return memo[n]
        return count_steps(n)
              


 


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def stairs(i):
        
            if i <= 2:
                return i
            if i in memo:
                return memo[i]
            
            memo[i] = stairs(i - 1) + stairs(i - 2)
            return memo[i]

        return stairs(n)
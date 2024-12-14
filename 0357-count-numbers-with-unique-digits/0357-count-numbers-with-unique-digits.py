class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        dp = [0] * (n+1)
        dp[1] = 10 

        comp = 9
        target = comp*comp

        for i in range(2,n+1):
            if i != 2:
                comp-=1
                target*=comp
            dp[i] = dp[i-1] + target
        
        return dp[n]
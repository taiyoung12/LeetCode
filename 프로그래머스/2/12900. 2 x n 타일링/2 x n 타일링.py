from collections import deque

def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    dp = deque()
    dp.append(1)
    dp.append(2)
    for i in range(2, n):
        # dp[i] = (dp[i-1] + dp[i-2])
        dp.append(dp.popleft() + dp[0])
    
    return dp[-1]%1000000007

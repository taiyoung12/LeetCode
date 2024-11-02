def solution(t):
    dp = [[0] * len(row) for row in t]
    dp[0][0] = t[0][0]
    
    for i in range(1, len(t)):
        for j in range(len(t[i])):
            if j == 0:
                dp[i][j] = dp[i-1][j] + t[i][j]
            elif j == len(t[i])-1:
                dp[i][j] = dp[i-1][j-1] + t[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + t[i][j]
    
    return max(dp[-1])
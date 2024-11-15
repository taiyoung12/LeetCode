def solution(n):
    if n == 1:
        return 1
    dp = [1]*n
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
    answer = dp[n-1] % 1234567
    return answer;


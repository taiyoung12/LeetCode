class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        answer = []
        def dfs(start, num):
            if start == n:
                if num not in answer:
                    return answer.append(num)
                else:
                    return 
            current = num % 10
            if current - k >= 0:
                dfs(start+1, num*10 + (current-k))
            if current + k < 10: 
                dfs(start+1, num*10 + (current+k))

        for i in range(1, 10):
            dfs(1, i)
        
        return answer
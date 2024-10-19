class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city):
            for i in range(len(isConnected)):
                if isConnected[city][i] == 1:
                    isConnected[city][i] = 0
                    isConnected[i][city] = 0 
                    dfs(i)

        city = len(isConnected)
        answer = 0 

        for i in range(city):
            if isConnected[i][i] == 1:
                dfs(i)
                answer+=1
        
        return answer 
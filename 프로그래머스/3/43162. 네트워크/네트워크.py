def dfs(target, i, n, computers):
    target[i]=True 
    
    for j in range(n):
        if j != i and computers[i][j] == 1 and target[j] == 0:
            dfs(target, j, n, computers)

def solution(n, computers):
    answer = 0
    target = [0] * n
    
    for i in range(n):
        if target[i] == 0:
            dfs(target, i, n, computers)
            answer+=1
    
    return answer
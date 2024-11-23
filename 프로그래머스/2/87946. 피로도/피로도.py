answer = 0
def dfs(comp, cnt, k, dungeons):
    global answer 
    
    answer = max(answer, cnt)
    
    for i in range(len(dungeons)):
        if comp[i] == 0 and k >= dungeons[i][0]:
            comp[i]=1
            dfs(comp, cnt+1, k-dungeons[i][1], dungeons)
            comp[i]=0
    
def solution(k, dungeons):
    global answer
    comp = [0]*len(dungeons)
    
    dfs(comp, 0, k, dungeons)
    
    return answer 
    
def solution(clothes):
    comp = dict()
    answer = 1
    target = 0
    
    row = len(clothes)
    col = len(clothes[0])
    
    for i in range(0, row):
        for j in range(0, col-1):
            if clothes[i][-1] not in comp:
                comp[clothes[i][-1]]=2
            else:
                comp[clothes[i][-1]]+=1
    
    if len(comp) == 1 :
        for c in comp:
            target += comp[c]
        return target-1
    
    for c in comp:
        answer*=comp[c]
        
    return answer-1
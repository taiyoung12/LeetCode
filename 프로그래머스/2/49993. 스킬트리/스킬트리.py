def solution(skill, trees):
    answer = 0 
    
    for tree in trees:
        temp = list(skill)
        flag = True 
        for t in tree: 
            if t in temp:
                if t != temp[0]:
                    flag = False 
                    break
                else:
                    temp.pop(0)
        if flag:
            answer+=1
        
    return answer
            
                
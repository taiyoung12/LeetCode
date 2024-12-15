def solution(p, s):
    answer = []
    count = 0
    time = 0 
    
    while len(p) > 0 : 
        
        if(p[0] + time*s[0]) >= 100:
            p.pop(0)
            s.pop(0)
            count+=1
            
        else : 
            if count > 0:
                answer.append(count)
                count=0
            time+=1
    answer.append(count)
    return answer
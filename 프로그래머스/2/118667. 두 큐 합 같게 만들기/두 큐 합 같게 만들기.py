from collections import deque

def solution(q1, q2):
    q1 = deque(q1)
    q2 = deque(q2)
    sum1 = sum(q1)
    sum2 = sum(q2)
    target = (sum1 + sum2) / 2
    if int(target) != target:
        return -1
    
    answer = 0 
    target = int(target)
    comp = 0
    
    for i in range(0,  300000): 
        if sum1 < sum2: 
            comp = q2.popleft()
            q1.append(comp)
            sum1+=comp
            sum2-=comp
            answer+=1 
        elif sum1 > sum2:
            comp = q1.popleft()
            q2.append(comp)
            sum1-=comp
            sum2+=comp
            answer+=1 
        else: 
            return answer 
    
    return -1
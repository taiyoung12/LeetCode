import math 

def solution(n, sts, w):
    answer = 0
    dists = []
    width = (1+2*w)
    
    for i in range(1, len(sts)):
        dists.append((sts[i]-w)-(sts[i-1]+w)-1)
    
    dists.append(sts[0]-w-1)
    dists.append(n-(sts[-1]+w))
    
    for dist in dists:
        if dist > 0:
            answer += math.ceil(dist/width)
    return answer
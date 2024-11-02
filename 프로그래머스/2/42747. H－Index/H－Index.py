def solution(cs):
    cs.sort()
    if cs[0] == cs[-1] and cs[-1] ==0:
        return 0
    
    index = 0
    while cs[index] != len(cs[index:]):
        if cs[index] > len(cs[index:]):
            return len(cs[index:])
        index+=1
    
    return cs[index]
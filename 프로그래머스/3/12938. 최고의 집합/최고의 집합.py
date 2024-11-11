def solution(n, s):    
    if s < 2 or n > s:
        return [-1]
    
    temp = []
    
    while n != 0:
        comp = s//n
        temp.append(comp)
        s -= comp 
        n -= 1
    
    return temp
def solution(es):
    ran = 1
    esLen = len(es)
    answer = set()
    
    while ran <= esLen:
        for i in range(esLen):
            if i + ran <= esLen:
                answer.add(sum(es[i:i+ran]))
            if i + ran > esLen-1:
                comp = ran - len(es[i:])
                answer.add(sum(es[:comp] + es[i:]))
        
        ran+=1
    
    return len(answer)
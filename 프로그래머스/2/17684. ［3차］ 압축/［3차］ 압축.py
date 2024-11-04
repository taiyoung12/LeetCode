def solution(msg):
    alphas = {'A': 1, 'B': 2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I': 9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
    
    answer = []
    index = 26
    i = 0
    
    while True:
        if i > len(msg)-1:
            break 
        for j in range(len(msg), i, -1):
            if msg[i:j] in alphas:
                answer.append(alphas[msg[i:j]])
                index+=1
                alphas[msg[i:j+1]] =index
                i=j
                break 
    
    return answer
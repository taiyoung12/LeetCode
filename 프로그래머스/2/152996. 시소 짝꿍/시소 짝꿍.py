def solution(weights):
    dic = {}
    answer=0
    
    for weight in weights:
        if weight in dic:
            dic[weight]+=1
        else:
            dic[weight]=1
            
    
    for weight in dic:
        if dic[weight] >1:
            answer += (dic[weight] * (dic[weight]-1))/2
        if weight*2 in dic:
            answer += (dic[weight] * (dic[2*weight]))
        if weight*2/3 in dic:
            answer += (dic[weight] * (dic[weight*2/3]))
        if weight*3/4 in dic:
            answer += (dic[weight] * (dic[weight*3/4]))
    
    return answer
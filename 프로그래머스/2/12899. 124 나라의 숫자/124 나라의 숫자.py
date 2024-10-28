def solution(n):
    answer = ""
    while n!= 0:
        remain = n%3
        print(remain)
        if remain == 0:
            answer+="4"
            n-=1
        else:    
            answer+=str(remain)
        n = (n//3)
        
    return answer[::-1]
import math

def verify(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def solution(n, k):
    c = ""
    answer = 0
    while n > 0:
        c+=str(n%k)
        n = n//k
    c = c[::-1]
    
    c = c.split("0")
    
    for t in c:
        if t != "1" and t != "":
            if verify(int(t)):
                answer+=1
    
    return answer
        
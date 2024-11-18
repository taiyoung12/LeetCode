def solution(s):
    answer = 0
    for i in range(len(s)):
        temp = list(s[i:] +s[:i])
        comp = []
        while temp:
            t = temp.pop(0)
            if len(comp) > 0 and t == ']' and comp[-1] == '[':
                comp.pop(-1)
            elif len(comp) > 0 and t  == ')' and comp[-1] == '(':
                comp.pop(-1)
            elif len(comp) > 0 and t == '}' and comp[-1] == '{':
                comp.pop(-1)
            else:
                comp.append(t)
        
        if len(comp) == 0:
            answer+=1

    return answer
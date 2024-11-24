def solution(files):
    comp = ["0", "1" , "2", "3", "4", "5", "6", "7", "8", "9"]
    target = []
    
    head = ""
    number = ""
    tail = ""
    
    while files:
        file = files.pop(0)
        
        for i in range(len(file)):
            if file[i] in comp:
                head = file[:i]
                number = file[i:]
                
                for j in range(len(number)):
                    if number[j] not in comp:
                        tail = number[j:]
                        number = number[:j]
                        break 
                target.append([head, number, tail])
            
                head = ""
                number = ""
                tail = ""
                break 
    
    target = sorted(target, key = lambda x:(x[0].lower(), int(x[1])))
    
    return  [''.join(t) for t in target]
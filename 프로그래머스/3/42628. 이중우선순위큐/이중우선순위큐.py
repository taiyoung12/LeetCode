def solution(operations):
    comp = []
    
    for op in operations: 
        t = op.split(" ")
        if t[0] == "I":
            comp.append(int(t[1]))
        if t[0] == "D" and t[1] == "1" and len(comp) !=0:
            comp.remove(max(comp))
        if t[0] == "D" and t[1] == "-1" and len(comp) !=0:
            comp.remove(min(comp))
    
    return [0, 0] if len(comp)==0 else [max(comp), min(comp)]
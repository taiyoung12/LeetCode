from itertools import permutations

def convert(exp, comp, stack):
    a = ""
    for e in exp:
        if e in "*+-":
            stack.append(a)
            comp.append(e)
            a = ""
        else:
            a += e
    stack.append(a)

def calculate(stack, comp, priority):
    stack = stack[:]
    comp = comp[:]

    for op in priority:
        i = 0
        while i < len(comp):
            if comp[i] == op:
                left = int(stack[i])
                right = int(stack[i + 1])
                if op == "*":
                    result = left * right
                elif op == "+":
                    result = left + right
                elif op == "-":
                    result = left - right
                
                stack[i] = result
                del stack[i + 1]
                del comp[i]
            else:
                i += 1
    return abs(stack[0])

def solution(exp):
    priorities = permutations(["*", "+", "-"])
    comp = []
    stack = []

    convert(exp, comp, stack)

    answers = []
    for priority in priorities:
        result = calculate(stack, comp, priority)
        answers.append(result)


    return max(answers)

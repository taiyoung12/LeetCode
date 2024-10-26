def convert(number):
    comp = ""
    while number: 
        comp += str(number % 2)
        number = number // 2
    return comp[::-1]
    
def solution(numbers):
    answer = []
    for number in numbers:
        current = number
        if number % 2 == 0:
            answer.append(number + 1)
        else:
            current = "0" + convert(number)
            idx = current.rfind("0")
            current = current[:idx] + "10" + current[idx + 2:]
            answer.append(int(''.join(current), 2))

    return answer
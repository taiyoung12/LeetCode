def re(records):
    users = dict()
    for record in records: 
        total = record.split(" ")
        if total[0] == 'Enter':
            if total[1] not in users: 
                users[total[1]] = total[2]
            else: 
                users[total[1]] = total[2]
        elif total[0] == 'Change':
            users[total[1]] = total[2]
    return users 

def solution(records):
    users = re(records)
    answer = []
    
    for record in records:
        total = record.split(" ")
        talk = ''
        if total[0] == 'Enter':
            talk = users[total[1]] + "님이 들어왔습니다."
        elif total[0] == 'Leave':
            talk = users[total[1]] + "님이 나갔습니다."
        else:
            continue 
        answer.append(talk)
    return answer
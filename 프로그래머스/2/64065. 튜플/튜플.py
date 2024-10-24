from collections import Counter

def solution(s):
    answer = []
    word_list = list(map(int, s.replace("}", "").replace("{", "").split(",")))
    count_dict = Counter(word_list).most_common()
    
    for d in count_dict:
        answer.append(d[0])
    
    return answer
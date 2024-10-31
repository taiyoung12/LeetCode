def solution(word):
    vowels = "AEIOU"
    word_list = []
    
    def dfs(current, length):
        if length > 5:
            return 
        word_list.append(current)
        
        for vowel in vowels: 
            dfs(current + vowel, length + 1)

    dfs("", 0)
    
    return word_list.index(word)
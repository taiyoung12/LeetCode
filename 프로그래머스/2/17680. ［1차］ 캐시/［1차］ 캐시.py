def update(caches, city, cacheSize, hit, hit_index): 
        c_len = len(caches)
        if c_len < cacheSize:
            caches.append(city)
        elif hit == True and c_len == cacheSize:
            caches.pop(hit_index)
            caches.append(city)
        else: 
            caches.pop(0)
            caches.append(city)

def solution(cacheSize, cities):    
    if cacheSize == 0:
        return len(cities)*5
            
    answer = 0
    caches = []
    hit = False 
    hit_index = 0
    for city in cities:
        city = city.lower()
        if city in caches:
            answer+=1
            hit = True
            hit_index = caches.index(city)
        else:
            answer+=5
            hit = False 
        update(caches, city, cacheSize, hit, hit_index)

    return answer 
        
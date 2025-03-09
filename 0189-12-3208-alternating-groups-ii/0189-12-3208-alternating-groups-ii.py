class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        length=len(colors)
        answer = 0 
        alt = 1 
        prev = colors[0]
        
        for i in range(1, length+k-1):
            index = i%length 
            if prev == colors[index]:
                alt=1 
            else:
                alt+=1
                
            answer+=(alt>=k)
            prev=colors[index]

        return answer
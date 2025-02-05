class Solution:
    def countAndSay(self, n: int) -> str:
        def convert(string: str) -> str:
            target=string[0]
            answer = ''
            comp = 1

            for i in range(1, len(string)):
                if target == string[i]:
                    comp+=1
                elif target != string[i]:
                    answer += (str(comp) + target)
                    target = string[i]
                    comp=1
            
            answer += (str(comp) + target)
            return answer 
        
        attempt = 1 
        answer = "1"

        while attempt != n:
         answer = convert(answer)
         attempt+=1

        return answer
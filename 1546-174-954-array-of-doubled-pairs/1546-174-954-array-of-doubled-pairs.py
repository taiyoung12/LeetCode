class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr = sorted(arr, key=abs)
        target = {}

        for number in arr :
            if number not in target:
                target[number] = 1
            else:
                target[number]+=1

        for number in arr:
            if target[number] == 0:
                continue

            comp = number*2
            if comp not in target or target[comp] == 0:
                return False
            
            target[comp]-=1
            target[number]-=1
        
        return True 
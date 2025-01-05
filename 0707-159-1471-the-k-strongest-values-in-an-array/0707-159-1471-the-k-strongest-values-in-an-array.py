class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        target={}
        arr.sort()
        medium = (len(arr)-1)//2
        answer = []
        
        for num in arr:
            comp = abs(num-arr[medium])
            if comp not in target:
                target[comp] = [num]
            else:
                target[comp].append(num)
        target = dict(sorted(target.items(), key=lambda x: x[0], reverse=True))
        
        for t in target:
            target[t].sort(reverse=True)
            for n in target[t]:
                answer.append(n)
        return answer[:k]
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 
        right = len(numbers) -1 
        answer = []

        while left < right : 
            comp = numbers[left] + numbers[right]
            if comp > target :
                right-=1
            if comp < target : 
                left+=1
            if comp == target : 
                answer.append(left+1)
                answer.append(right+1)
                break 
        return answer
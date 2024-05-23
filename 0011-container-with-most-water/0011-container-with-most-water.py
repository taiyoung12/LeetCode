class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0 
        right = len(height)-1
        answer = [left, right]
        while left < right :             
            sum1 = (answer[1] - answer[0]) * (min(height[answer[0]], height[answer[1]]))
            if height[left] < height[right]: 
                left+=1 
            else:
                right-=1    
            sum2 = (right - left) * (min(height[left], height[right]))
            if sum1 < sum2 : 
                answer[0]=left
                answer[1]=right
        
        return (answer[1] - answer[0]) * (min(height[answer[0]], height[answer[1]]))
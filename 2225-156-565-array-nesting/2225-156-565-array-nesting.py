class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        def dfs(visited, index, nums, comp):
            if visited[nums[index]] == 0:
                visited[nums[index]]=1
                comp+=1
                return dfs(visited, nums[index], nums, comp)
            else:
                return comp

        res = 0
        visited = [0]*len(nums)
        
        for i in range(len(nums)):
            if visited[i] == 0:
                visited[i]=1
                comp = 1
                comp = dfs(visited, i, nums, comp)
                res = max(comp, res)

        return res 
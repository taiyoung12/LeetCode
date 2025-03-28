class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        grids = []
        answer = 0

        for g in grid:
            for number in g:
                grids.append(number)
        
        grids = sorted(grids)

        m = len(grids)//2

        for number in grids:
            if number % x != grids[m] % x:
                return -1
        
            answer += abs(grids[m]-number) // x
        
        return answer

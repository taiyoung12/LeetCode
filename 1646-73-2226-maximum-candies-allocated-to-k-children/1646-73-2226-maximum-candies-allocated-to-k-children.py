class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        
        low, high = 1, max(candies)
        answer = 0 

        def sol(mid):
            children = 0
            for c in candies:
                children += (c // mid)
            return k <= children

        while low <= high:
            mid = (low+high) // 2
            if sol(mid):
                answer = mid 
                low = mid+1
            else:
                high = mid-1

        return answer 
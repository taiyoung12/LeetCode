class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_num = prices[0]
        comp = 0

        for price in prices : 
            if min_num > price : 
                min_num = price 
            diff = price - min_num
            if comp < diff : 
                comp = diff 
        return comp 
        
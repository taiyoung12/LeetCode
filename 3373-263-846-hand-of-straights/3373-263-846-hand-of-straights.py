class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        keys = sorted(count.keys())
        
        for key in keys:
            while count[key] > 0:
                for i in range(groupSize):
                    if count[key+i] <=0:
                        return False 
                    count[key+i]-=1
        
        return True 
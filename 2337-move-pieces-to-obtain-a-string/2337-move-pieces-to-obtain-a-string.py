class Solution:
    def canChange(self, start: str, target: str) -> bool:
        start_index = []
        target_index = []
        for i, v in enumerate(start):
            if v in "LR":
                start_index.append((i, v))
        for i, v in enumerate(target):
            if v in "LR":
                target_index.append((i, v))
        
        if len(start_index) != len(target_index):
            return False 
        
        for (i, s), (j, t) in zip(start_index, target_index):
            if s != t:
                return False 
            if s == "L" and i < j:
                return False 
            if s == "R" and i > j:
                return False 

        return True 
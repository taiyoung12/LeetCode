class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        targets = dict()

        for string in strs:
            comp = ''.join(sorted(string))
            if comp not in targets:
                targets[comp] = [string]
            else:
                targets[comp].append(string)
        
        for target in targets:
            answer.append(targets.get(target))
            

        return answer
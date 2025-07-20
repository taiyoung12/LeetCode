class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = {}
        answer = []
        for i in range(0, len(strs)):
            target = ''.join(sorted(strs[i]))

            if target not in temp:
                temp[target] = [i]
            else :
                temp[target].append(i)

        for index in temp:
            target = []
            for j in temp[index]:
                target.append(strs[j])
            answer.append(target)
        
        return answer
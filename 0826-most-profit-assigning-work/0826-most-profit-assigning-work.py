class Solution:
    def maxProfitAssignment(self, d: List[int], p: List[int], w: List[int]) -> int:
        wm = max(w)
        hap = dict()
        answer = 0

        for i in range(len(d)):
            if wm < d[i]:
                continue 
            if d[i] not in hap:
                hap[d[i]] = p[i]
            else:
                hap[d[i]] = max(hap[d[i]], p[i])

        if not hap:
            return answer

        hap_dict = dict(sorted(hap.items(), key = lambda x:x[1], reverse = True))
        w.sort()

        while w:
            worker = w.pop(0)

            for h in hap_dict:
                if h <= worker:
                    answer += hap_dict[h]
                    break 

        return answer
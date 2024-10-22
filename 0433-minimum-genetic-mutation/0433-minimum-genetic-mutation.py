class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        q = deque([(startGene, 0)])
        bank = set(bank)

        while q: 
            dq, depth = q.popleft()
            if dq == endGene:
                return depth

            for i in range(0, 8):
                for gene in 'ACGT':
                    comp = dq[0:i] + gene + dq[i+1:]
                    if comp in bank:
                        bank.remove(comp)
                        q.append((comp, depth+1))

        return -1
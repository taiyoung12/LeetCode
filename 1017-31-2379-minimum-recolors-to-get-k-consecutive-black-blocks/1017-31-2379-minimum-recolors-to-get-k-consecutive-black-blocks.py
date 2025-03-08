class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        answer = 101
        iteration = len(blocks) - k + 1 

        for i in range(0, iteration):
            target = blocks[i:i+k]
            comp = 0
            for t in target:
                if t == "W":
                    comp+=1
            answer = min(comp, answer)

        return answer 
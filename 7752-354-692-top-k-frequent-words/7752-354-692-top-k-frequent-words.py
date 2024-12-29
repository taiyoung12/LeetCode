class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordsHash = Counter(words)
        answer = [w[0] for w in sorted(wordsHash.items(), key=lambda x:(-x[1], x[0]))]
        
        return answer[:k]
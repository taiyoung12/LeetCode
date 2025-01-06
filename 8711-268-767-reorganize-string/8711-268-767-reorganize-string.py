from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        char_count = Counter(s)
        max_heap = [(-freq, char) for char, freq in char_count.items()]
        
        heapq.heapify(max_heap)
        
        prev_char, prev_freq = None, 0
        result = []
        
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            result.append(char)
            
            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))
            
            prev_char, prev_freq = char, freq + 1

        result_str = ''.join(result)
        if len(result_str) != len(s):
            return ""
        
        return result_str

from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_freq = max(task_counts.values())  
        num_max_tasks = sum(1 for count in task_counts.values() if count == max_freq)
        
        part_count = max_freq - 1  
        empty_slots = part_count * (n - (num_max_tasks - 1))
        available_tasks = len(tasks) - max_freq * num_max_tasks  
        idle_slots = max(0, empty_slots - available_tasks) 
        
        return len(tasks) + idle_slots 

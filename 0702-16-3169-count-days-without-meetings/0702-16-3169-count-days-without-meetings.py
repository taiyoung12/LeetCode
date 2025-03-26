class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        if not meetings:
            return days

        meetings.sort()

        merged = [meetings[0]]
        for start, end in meetings[1:]:
            last_start, last_end = merged[-1]
            if start <= last_end:
                merged[-1][1] = max(last_end, end)
            else:
                merged.append([start, end])

        total_meeting_days = sum(end - start + 1 for start, end in merged)

        return days - total_meeting_days
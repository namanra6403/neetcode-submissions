"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda interval: interval.start)

        endtime = []
        max_rooms = 0

        for interval in intervals:
            start = interval.start
            end = interval.end

            while endtime and endtime[0] <= start:
                heapq.heappop(endtime)

            heapq.heappush(endtime, end)

             # Heap size = rooms currently being used
            max_rooms = max(max_rooms, len(endtime))

        return max_rooms
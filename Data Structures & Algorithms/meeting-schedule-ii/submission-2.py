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
        minHeap = []
        max_len = 0

        for interval in sorted(intervals, key=lambda x: x.start):
            while minHeap and minHeap[0] <= interval.start:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, interval.end)
            max_len = max(max_len, len(minHeap))

        return max_len

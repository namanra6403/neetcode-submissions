"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # defintley iterating using for loop
        # keep track of the upper limit number of the tuple before current
        # return false if there is a conflict and return true if we go through the loop and don't find issues
        prev = float("-inf")
        for interval in sorted(intervals, key=lambda x: x.start):
            if interval.start < prev:
                return False
            prev = interval.end


        return True

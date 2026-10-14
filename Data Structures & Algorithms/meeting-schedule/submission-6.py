"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        agenda = []
        for interval in intervals:
            agenda.append((interval.start, interval.end))
        agenda.sort()
        for i in range(len(agenda)-1):
            first_interval_end = agenda[i][1]
            second_interval_start = agenda[i+1][0]
            if first_interval_end > second_interval_start:
                return False
        return True



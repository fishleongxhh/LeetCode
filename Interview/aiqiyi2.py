# -*- coding: utf-8 -*-

import sys

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def eraseOverlapIntervals(intervals):
    end = float('-inf')
    erased = 0
    for i in sorted(intervals, key=lambda i: i.end):
        if i.start >= end:
            end = i.end
        else:
            erased += 1
    return len(intervals) - erased

N = int(sys.stdin.readline().strip())
intervals = []
for i in range(N):
    record = [int(i) for i in sys.stdin.readline().strip().split('  ')]
    print(record)
    if record[0] > record[1]:
        record[1], record[0] = record[0], record[1]
    intervals.append(Interval(record[0], record[1]))

print(eraseOverlapIntervals(intervals))

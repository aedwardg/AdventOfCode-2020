import math
from collections import deque

def part1(data):
    jolts = parse_jolts(data)
    
    diffs = {1: 0, 2: 0, 3: 0}
    
    for i in range(len(jolts) - 1):
        difference = jolts[i + 1] - jolts[i]
        diffs[difference] += 1

    return diffs[1] * diffs[3]


# inspired by @salt-die's solution for Day 10 pt 2
def part2(data):
    jolts = parse_jolts(data)
    rev = reversed(jolts)
    counts = deque(((next(rev), 1), ), maxlen=3)

    for i in rev:
        summed = sum(ct for jolt, ct in counts if jolt - i <= 3)
        counts.append((i, summed))
    
    return summed


def parse_jolts(data):
    lines = data.splitlines()
    jolts = deque(sorted([int(i) for i in lines]))
    jolts.appendleft(0)
    jolts.append(max(jolts) + 3)
    return jolts

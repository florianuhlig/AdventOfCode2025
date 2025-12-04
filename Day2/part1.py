def is_invalid_id(n: int) -> bool:
    s = str(n)
    length = len(s)
    if length % 2 != 0:
        return False
    half = length // 2
    first_part = s[:half]
    second_part = s[half:]
    return first_part == second_part and not first_part.startswith('0')

def sum_invalid_ids(ranges):
    total = 0
    for r in ranges:
        start, end = map(int, r.split('-'))
        for x in range(start, end + 1):
            if is_invalid_id(x):
                total += x
    return total

import sys
input_line = None
if len(sys.argv) > 1:
    with open(sys.argv[1]) as f:
        input_line = f.read().strip()
        ranges = [r for r in input_line.split(',') if r]
        print(sum_invalid_ids(ranges))
else:
    input_line = sys.stdin.read().strip()

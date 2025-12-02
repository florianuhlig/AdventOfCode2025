def count_zero_positions(rotations):
    position = 50 # Start position
    zero_count = 0 # Zero Count
    for move in rotations:
        direction, dist = move[0], int(move[1:])
        if direction == 'L':
            position = (position - dist) % 100
        elif direction == 'R':
            position = (position + dist) % 100
        if position == 0:
            zero_count += 1
    return zero_count

import sys
# Reads lines from filename given as the argument, or from stdin
if len(sys.argv) > 1:
    with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f if line.strip()]
        print(count_zero_positions(lines))
else:
        print("NO FILE INSERTED")

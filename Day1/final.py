def part1(rotations):
    position = 50
    zero_count = 0
    for move in rotations:
        direction, dist = move[0], int(move[1:])
        if direction == 'L':
            position = (position - dist) % 100
        elif direction == 'R':
            position = (position + dist) % 100
        if position == 0:
            zero_count += 1
    return zero_count

def part2(rotations):
    position = 50
    for move in rotations:
        direction, dist = move[0], int(move[1:])
        if direction == 'L':
            position = (position - dist) % 100
        elif direction == 'R':
            position = (position + dist) % 100
    return position

import sys
if len(sys.argv) > 1:
    with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f if line.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))
else:
        print("NO FILE INSERTED")

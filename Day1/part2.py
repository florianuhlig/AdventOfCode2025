def part2_safe(rotations):
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
        print(part2_safe(lines))
else:
    print("NO INPUT GIVEN")

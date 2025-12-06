import sys

pos = 50

with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        d, n = line[0], int(line[1:])
        pos = (pos - n if d == 'L' else pos + n) % 100

print(pos)

import sys

pos = 50
count = 0

with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        d, n = line[0], int(line[1:])
        pos = (pos - n if d == 'L' else pos + n) % 100
        if pos == 0:
            count += 1

print(count)

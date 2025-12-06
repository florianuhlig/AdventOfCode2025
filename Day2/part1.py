import sys

def is_invalid(n):
    s = str(n)
    if len(s) % 2 != 0:
        return False
    mid = len(s) // 2
    return s[:mid] == s[mid:]

total = 0
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    for part in f.read().strip().split(','):
        lo, hi = map(int, part.split('-'))
        for n in range(lo, hi + 1):
            if is_invalid(n):
                total += n

print(total)

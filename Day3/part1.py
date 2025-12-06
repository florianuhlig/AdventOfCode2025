import sys

total = 0
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    for line in f:
        digits = line.strip()
        if not digits:
            continue
        best = 0
        for i in range(len(digits) - 1):
            max_right = max(int(digits[j]) for j in range(i + 1, len(digits)))
            best = max(best, 10 * int(digits[i]) + max_right)
        total += best

print(total)

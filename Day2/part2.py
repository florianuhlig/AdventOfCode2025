def generate_repeated_ids(max_digits=12):
    """Generate all possible invalid IDs (repeated sequences) up to max_digits."""
    invalid_ids = []
    for half_len in range(1, max_digits//2 + 1):
        for i in range(10**(half_len-1), 10**half_len):  # No leading zeros
            num_str = str(i)
            repeated = int(num_str + num_str)
            invalid_ids.append(repeated)
    return invalid_ids

def sum_invalid_in_range(start, end, invalid_ids):
    """Sum invalid IDs within a specific range efficiently."""
    total = 0
    for invalid_id in invalid_ids:
        if start <= invalid_id <= end:
            total += invalid_id
    return total

def sum_all_invalid(ranges, invalid_ids):
    total = 0
    for r in ranges:
        start, end = map(int, r.split('-'))
        total += sum_invalid_in_range(start, end, invalid_ids)
    return total

if __name__ == "__main__":
    import sys
    
    # Generate all possible invalid IDs up to reasonable size
    ALL_INVALID_IDS = generate_repeated_ids(14)
    
    input_line = None
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            input_line = f.read().strip()
    else:
        input_line = sys.stdin.read().strip()
    
    ranges = [r.strip() for r in input_line.split(',') if r.strip()]
    print(sum_all_invalid(ranges, ALL_INVALID_IDS))


"""
Advent of Code 2025 - Day 3: Lobby (Part 2)
Solves the battery joltage puzzle with 12-digit selection for a given input file.
"""

def max_joltage_12_digits(line):
    """
    Find the maximum 12-digit joltage for a single bank of batteries.
    We need to choose exactly 12 digits from the input line (maintaining their order)
    such that the resulting 12-digit number is maximized.
    Uses a greedy stack-based approach: scan left to right, remove smaller digits
    from the stack when a larger digit appears, allowing us to position larger
    digits in more significant places.
    Args:
        line: A string of digits (e.g., "987654321111111")
    Returns:
        The maximum 12-digit joltage possible from this bank
    """
    digits = line.strip()
    n = len(digits)
    target_length = 12
    to_remove = n - target_length
    # Handle edge case
    if n < target_length:
        return 0  # Can't select 12 digits from fewer than 12
    # Stack-based greedy approach
    # We build the result by maintaining a stack of selected digits
    stack = []
    removals_left = to_remove
    for i in range(n):
        current_digit = digits[i]
        # Remove smaller digits from stack if:
        # 1. We still have removals available
        # 2. The current digit is larger than the top of the stack
        while stack and removals_left > 0 and stack[-1] < current_digit:
            stack.pop()
            removals_left -= 1
        stack.append(current_digit)
    # If we still have removals left after scanning (meaning we never encountered a larger digit), remove from the end (keeps the largest leading digits)
    while removals_left > 0:
        stack.pop()
        removals_left -= 1
    # Stack now contains exactly 12 digits in order
    result = int(''.join(stack))
    return result


def solve(filename):
    """
    Solve the puzzle by reading the input file and calculating total output joltage.
    Args:
        filename: Path to the input file (one bank per line)
    Returns:
        The total output joltage (sum of max 12-digit joltage per bank)
    """
    total_joltage = 0
    bank_count = 0

    try:
        with open(filename, 'r') as f:
            for line_num, line in enumerate(f, start=1):
                line = line.strip()
                # Skip empty lines
                if not line:
                    continue
                # Validate that the line contains only digits
                if not line.isdigit():
                    print(f"Warning: Line {line_num} contains non-digit characters: {line}")
                    continue
                # Check if we have at least 12 digits
                if len(line) < 12:
                    print(f"Warning: Line {line_num} has only {len(line)} digits (need at least 12): {line}")
                    continue
                bank_count += 1
                max_volt = max_joltage_12_digits(line)
                total_joltage += max_volt
                print(f"Bank {bank_count}: {line} ({len(line)} digits) → max 12-digit joltage = {max_volt}")
        print(f"\n{'='*60}")
        print(f"Total output joltage: {total_joltage}")
        print(f"{'='*60}")
        return total_joltage

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


result = solve("input.txt")

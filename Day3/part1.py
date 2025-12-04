"""
Advent of Code 2025 - Day 3: Lobby
Solves the battery joltage puzzle for a given input file.
"""
def max_joltage_per_bank(line):
    """
    Find the maximum joltage for a single bank of batteries.
    For a line of digits, choose two batteries at positions i < j
    to form the largest two-digit number 10*d[i] + d[j].
    Args:
        line: A string of digits (e.g., "987654321111111")
    Returns:
        The maximum joltage (two-digit number) possible from this bank
    """
    digits = line.strip()
    if len(digits) < 2:
        return 0  # Need at least 2 digits to form a number
    max_voltage = 0

    # Try each position as the tens digit
    for i in range(len(digits) - 1):  # i must have at least one digit to its right
        tens_digit = int(digits[i])

        # Find the maximum digit to the right of position i
        max_ones = max(int(digits[j]) for j in range(i + 1, len(digits)))

        # Calculate the voltage using this tens digit and the best ones digit
        voltage = 10 * tens_digit + max_ones
        max_voltage = max(max_voltage, voltage)
    return max_voltage


def solve(filename):
    """
    Solve the puzzle by reading the input file and calculating total output joltage.
    Args:
        filename: Path to the input file (one bank per line)
    Returns: The total output joltage (sum of max joltage per bank)
    """
    total_joltage = 0
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
                max_volt = max_joltage_per_bank(line)
                total_joltage += max_volt
                print(f"Bank {line_num}: {line} → max joltage = {max_volt}")
        print(f"\n{'='*50}")
        print(f"Total output joltage: {total_joltage}")
        print(f"{'='*50}")
        return total_joltage

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


result = solve("input.txt")


"""
Advent of Code 2025 - Day 4: Printing Department
Part 2: Remove rolls iteratively until none can be accessed

A roll of paper (@) can be accessed and removed if there are FEWER than 4 rolls
in the 8 adjacent positions. As rolls are removed, more rolls may become accessible.
"""

def count_adjacent_at_symbol(grid, row, col):
    """
    Count the number of '@' symbols in the 8 adjacent positions.
    
    Args:
        grid: List of strings representing the grid
        row: Row index
        col: Column index
    
    Returns:
        Number of '@' symbols in adjacent positions (0-8)
    """
    count = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    directions = [
        (-1, -1), (-1, 0), (-1, 1),  # North row
        (0, -1),          (0, 1),    # Same row
        (1, -1),  (1, 0),  (1, 1)    # South row
    ]
    
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == '@':
                count += 1
    
    return count


def find_accessible_rolls(grid):
    """
    Find all rolls that can be accessed by a forklift.
    
    A roll can be accessed if it has fewer than 4 adjacent rolls.
    
    Args:
        grid: List of strings representing the grid
    
    Returns:
        List of (row, col) tuples for accessible rolls
    """
    accessible = []
    rows = len(grid)
    
    for row in range(rows):
        for col in range(len(grid[row])):
            if grid[row][col] == '@':
                adjacent_count = count_adjacent_at_symbol(grid, row, col)
                if adjacent_count < 4:
                    accessible.append((row, col))
    
    return accessible


def remove_rolls(grid, positions):
    """
    Remove rolls at specified positions.
    
    Args:
        grid: List of strings representing the grid
        positions: List of (row, col) tuples to remove
    
    Returns:
        New grid with specified positions changed to '.'
    """
    new_grid = [list(row) for row in grid]
    for row, col in positions:
        new_grid[row][col] = '.'
    return [''.join(row) for row in new_grid]


def solve_part1(grid):
    """
    Find all rolls of paper that can be accessed by a forklift (no removal).
    
    Args:
        grid: List of strings representing the grid
    
    Returns:
        Number of initially accessible rolls
    """
    return len(find_accessible_rolls(grid))


def solve_part2(grid, verbose=False):
    """
    Simulate removing rolls iteratively until no more can be removed.
    
    Each iteration:
    1. Find all currently accessible rolls (fewer than 4 adjacent)
    2. Remove them all simultaneously
    3. Repeat until no accessible rolls remain
    
    Args:
        grid: List of strings representing the grid
        verbose: If True, print details of each iteration
    
    Returns:
        Total number of rolls removed
    """
    grid = [str(row) for row in grid]  # Ensure grid is list of strings
    total_removed = 0
    iteration = 0
    
    while True:
        accessible = find_accessible_rolls(grid)
        if not accessible:
            break
        
        iteration += 1
        removed_this_round = len(accessible)
        total_removed += removed_this_round
        
        if verbose:
            print(f"Iteration {iteration}: Remove {removed_this_round} rolls (total: {total_removed})")
        
        # Remove all accessible rolls simultaneously
        grid = remove_rolls(grid, accessible)
    
    return total_removed


def load_grid(filename):
    """
    Load the grid from a file.
    
    Args:
        filename: Path to the input file
    
    Returns:
        List of strings representing the grid
    """
    try:
        with open(filename, 'r') as f:
            grid = [line.rstrip('\n') for line in f]
        return grid
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


def main():
    """Main function to solve both parts"""
    grid = load_grid("input.txt")
    
    if grid is None:
        return
    
    print(f"Grid dimensions: {len(grid)} rows x {len(grid[0]) if grid else 0} columns")
    
    # Part 1: Count initially accessible rolls
    part1_result = solve_part1(grid)
    print(f"\nPart 1 - Rolls accessible on first pass: {part1_result}")
    
    # Part 2: Remove all rolls iteratively
    print(f"\nPart 2 - Simulating iterative removal:")
    part2_result = solve_part2(grid, verbose=True)
    print(f"\nPart 2 - Total rolls removed: {part2_result}")


if __name__ == "__main__":
    main()

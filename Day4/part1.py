"""
Advent of Code 2025 - Day 4: Printing Department
Finds rolls of paper that can be accessed by forklifts.

A roll of paper (@) can be accessed if there are FEWER than 4 rolls
in the 8 adjacent positions.
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
    
    # All 8 adjacent positions (North, NorthEast, East, SouthEast, South, SouthWest, West, NorthWest)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),  # North row
        (0, -1),          (0, 1),    # Same row
        (1, -1),  (1, 0),  (1, 1)    # South row
    ]
    
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        # Check bounds and if the adjacent cell contains '@'
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == '@':
                count += 1
    
    return count


def solve_part1(grid):
    """
    Find all rolls of paper that can be accessed by a forklift.
    
    A roll can be accessed if it has fewer than 4 adjacent rolls.
    
    Args:
        grid: List of strings representing the grid
    
    Returns:
        Number of accessible rolls
    """
    accessible = 0
    rows = len(grid)
    
    for row in range(rows):
        for col in range(len(grid[row])):
            if grid[row][col] == '@':
                # Check if this roll can be accessed
                adjacent_count = count_adjacent_at_symbol(grid, row, col)
                if adjacent_count < 4:
                    accessible += 1
    
    return accessible


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


def visualize_solution(grid):
    """
    Print a visualization of the solution where:
    - 'x' marks accessible rolls
    - '@' marks inaccessible rolls (4+ adjacent)
    - '.' remains as '.'
    
    Args:
        grid: List of strings representing the grid
    """
    print("\nVisualization (x = accessible, @ = not accessible):")
    rows = len(grid)
    
    for row in range(rows):
        line = ""
        for col in range(len(grid[row])):
            if grid[row][col] == '@':
                adjacent_count = count_adjacent_at_symbol(grid, row, col)
                if adjacent_count < 4:
                    line += "x"
                else:
                    line += "@"
            else:
                line += grid[row][col]
        print(line)


def main():
    """Main function to solve the puzzle"""
    grid = load_grid("input.txt")
    
    if grid is None:
        return
    
    print(f"Grid dimensions: {len(grid)} rows x {len(grid[0]) if grid else 0} columns")
    
    result = solve_part1(grid)
    
    print(f"\nNumber of rolls that can be accessed by a forklift: {result}")
    
    # Optionally show visualization
#    visualize_solution(grid)


if __name__ == "__main__":
    main()

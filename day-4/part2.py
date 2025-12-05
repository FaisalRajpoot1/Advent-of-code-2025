def count_accessible_positions(grid):
    """Return a list of coordinates (r,c) of accessible rolls of paper."""
    rows = len(grid)
    cols = len(grid[0])
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    accessible = []

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue
            count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == '@':
                        count += 1
            if count < 4:
                accessible.append((r, c))
    return accessible


def total_removed_paper(grid):
    """Return the total number of rolls that can be removed iteratively."""
    # Convert grid to list of lists for mutability
    grid = [list(row) for row in grid]
    total_removed = 0

    while True:
        accessible = count_accessible_positions(grid)
        if not accessible:
            break
        total_removed += len(accessible)
        # Remove all accessible rolls
        for r, c in accessible:
            grid[r][c] = '.'

    return total_removed




input_file_path = "input.txt"

with open(input_file_path, "r") as f:
    content = f.read().strip().splitlines()

result = total_removed_paper(content)

print(f"Total rolls of paper removed: {result}")

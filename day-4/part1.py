def count_accessible_rolls(grid):
    rows = len(grid)
    cols = len(grid[0])

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    accessible = 0

    for r in range(rows):
        for c in range(cols):

            if grid[r][c] != '@':
                continue

            adjacent = 0

            # Count adjacent '@' rolls
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == '@':
                        adjacent += 1

            # Accessible if less than 4 neighbors
            if adjacent < 4:
                accessible += 1

    return accessible


input_file_path = "input.txt"  

with open(input_file_path, "r") as f:
    content = f.read().strip().splitlines()

result = count_accessible_rolls(content)

print(f"Number of accessible paper rolls: {result}")

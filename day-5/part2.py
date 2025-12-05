def count_total_fresh_ids(file_path):
    with open(file_path, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    # Remove empty lines at the top or bottom if any
    while lines and lines[-1] == "":
        lines.pop()

    # Find blank line that separates ranges and IDs
    blank_index = lines.index("")
    range_lines = lines[:blank_index]

    # Parse ranges
    ranges = []
    for r in range_lines:
        start, end = map(int, r.split("-"))
        ranges.append((start, end))

    # Merge overlapping ranges
    ranges.sort()
    merged = []

    current_start, current_end = ranges[0]

    for start, end in ranges[1:]:
        if start <= current_end:  # overlapping
            current_end = max(current_end, end)
        else:  # no overlap
            merged.append((current_start, current_end))
            current_start, current_end = start, end

    merged.append((current_start, current_end))

    # Count total unique fresh IDs
    total_fresh = 0
    for start, end in merged:
        total_fresh += (end - start + 1)

    return total_fresh


# if __name__ == "__main__":
#     file_name = input("Enter input file name: ").strip()
#     result = count_total_fresh_ids(file_name)
#     print(f"Number of fresh ingredients: {result}")

if __name__ == "__main__":
    result = count_total_fresh_ids("input.txt")
    print(f"Number of fresh ingredients: {result}")
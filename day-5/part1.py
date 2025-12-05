def count_fresh_ingredients(file_path):
    with open(file_path, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    # Split the ranges and ingredient IDs by the blank line
    blank_index = lines.index("")
    range_lines = lines[:blank_index]
    ingredient_lines = lines[blank_index+1:]

    # Parse ranges
    ranges = []
    for r in range_lines:
        start, end = map(int, r.split("-"))
        ranges.append((start, end))

    # Parse ingredient IDs
    ingredients = list(map(int, ingredient_lines))

    fresh_count = 0

    for ing in ingredients:
        # Check if ing falls inside ANY range
        if any(start <= ing <= end for start, end in ranges):
            fresh_count += 1

    return fresh_count



if __name__ == "__main__":
    result = count_fresh_ingredients("input.txt")
    print(f"Number of fresh ingredients: {result}")

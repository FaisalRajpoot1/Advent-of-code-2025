def solve(rotations):
    dial = 50  # starting position
    part1_count = 0
    part2_count = 0

    for rot in rotations:
        direction = rot[0]
        amount = int(rot[1:])

        # Determine movement direction
        step = -1 if direction == 'L' else 1

        # --- PART 2: Count every click that lands on 0 ---
        for _ in range(amount):
            dial = (dial + step) % 100
            if dial == 0:
                part2_count += 1

        # --- PART 1: Count only if final dial = 0 ---
        if dial == 0:
            part1_count += 1

    return part1_count, part2_count


# --------------------------
# READ FROM A FILE
# --------------------------

def main():
    # Change input.txt to your filename
    filename = "input-day-1.txt"

    with open(filename, "r") as f:
        rotations = [line.strip() for line in f.readlines() if line.strip()]

    part1, part2 = solve(rotations)

    print("Part 1 answer:", part1)
    print("Part 2 answer:", part2)


if __name__ == "__main__":
    main()

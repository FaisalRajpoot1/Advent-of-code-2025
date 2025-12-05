def max_k_digits(line, k=12):
    """Return the lexicographically largest subsequence of length k."""
    digits = line.strip()
    to_remove = len(digits) - k
    stack = []

    for d in digits:
        # Remove smaller digits if allowed
        while to_remove > 0 and stack and stack[-1] < d:
            stack.pop()
            to_remove -= 1
        stack.append(d)

    # Cut to exactly k digits
    return int("".join(stack[:k]))


def total_joltage_part2(lines):
    total = 0
    for line in lines:
        line = line.strip()
        if line:
            total += max_k_digits(line, 12)
    return total



input_file_path = "input.txt"  


with open(input_file_path, "r") as f:
    content = f.read().strip().splitlines()

result = total_joltage_part2(content)

print(f"Total Output Joltage (Part 2): {result}")

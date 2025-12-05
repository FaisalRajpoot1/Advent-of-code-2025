def get_max_two_digit(line):
    """Return the largest 2-digit number formed by picking two digits in order."""
    digits = line.strip()
    best = -1

    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):
            num = int(digits[i] + digits[j])
            if num > best:
                best = num

    return best


def total_joltage(lines):
    total = 0
    for line in lines:
        line = line.strip()
        if line:
            total += get_max_two_digit(line)
    return total




input_file_path = "input.txt"    


with open(input_file_path, "r") as f:
    content = f.read().strip().splitlines()
    
result = total_joltage(content)

print(f"Total Output Joltage: {result}")

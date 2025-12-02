def is_invalid_id_part2(n):
    """Check if a number is made of some sequence of digits repeated at least twice."""
    s = str(n)
    length = len(s)
    
    # Try all possible sequence lengths from 1 up to half the number length
    for seq_len in range(1, length // 2 + 1):
        if length % seq_len == 0:
            times = length // seq_len
            if s[:seq_len] * times == s:
                return True
    return False

def sum_invalid_ids_part2(ranges):
    total = 0
    for r in ranges:
        start, end = map(int, r.split('-'))
        for n in range(start, end + 1):
            if is_invalid_id_part2(n):
                total += n
    return total

# Specify your input file path here
input_file_path = "input.txt"

# Read the file
with open(input_file_path, 'r') as f:
    content = f.read().strip()

# Split the ranges by comma
ranges = content.split(',')

# Calculate the sum of invalid IDs for Part 2
result = sum_invalid_ids_part2(ranges)

print(f"Sum of invalid IDs (Part 2): {result}")

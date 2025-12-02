def is_invalid_id(n):
    """Check if a number is made of a repeated sequence of digits."""
    s = str(n)
    length = len(s)
    
    # Only even length numbers can be repeated halves
    if length % 2 != 0:
        return False
    
    half = length // 2
    return s[:half] == s[half:]

def sum_invalid_ids(ranges):
    total = 0
    for r in ranges:
        start, end = map(int, r.split('-'))
        for n in range(start, end + 1):
            if is_invalid_id(n):
                total += n
    return total

# Specify your input file path here
input_file_path = "input.txt"

# Read the file
with open(input_file_path, 'r') as f:
    content = f.read().strip()

# Split the ranges by comma
ranges = content.split(',')

# Calculate the sum of invalid IDs
result = sum_invalid_ids(ranges)

print(f"Sum of invalid IDs: {result}")

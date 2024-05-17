memo = {}  # Memoization dictionary to store computed cycle lengths

def cycle_length(n):
    if n in memo:
        return memo[n]
    length = 1
    original_n = n
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        length += 1
    memo[original_n] = length
    return length

def max_cycle_length(i, j):
    max_length = 0
    for num in range(min(i, j), max(i, j) + 1):
        # Iterate from smaller to larger number
        current_length = cycle_length(num)
        if current_length > max_length:
            max_length = current_length
    return max_length

# Reading input pairs and calculating maximum cycle lengths
while True:
    try:
        line = input().strip()
        if not line:
            continue
        i, j = map(int, line.split())
        max_length = max_cycle_length(i, j)
        print(i, j, max_length)
    except EOFError:
        break
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter two integers separated by a space.")

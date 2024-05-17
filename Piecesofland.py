def binomial_coefficient(n, k):
    if k > n // 2:
        k = n - k
    result = 1
    for i in range(1, k + 1):
        result *= (n - k + i)
        result //= i
    return result

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the number of rows for the current test case
    row = int(input())
    # Calculate the number of columns to consider (minimum of row and 5)
    col = min(row, 5)
    total = 0
    # Calculate the total number of ways to choose lines
    for j in range(col):
        total += binomial_coefficient(row - 1, j)
    # If total is 0, increment by 1
    if total == 0:
        total += 1
    # Print the result for the current test case
    print(total)

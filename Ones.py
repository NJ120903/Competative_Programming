# Function to find the smallest integer x such that p = 111...1 (x times) is divisible by n
def find_smallest_multiple(n):
    remainder = 1 % n
    x = 1
    while remainder != 0:
        x += 1
        remainder = (remainder * 10 + 1) % n
    return x

# Process test cases
def process_test_cases():
    while True:
        try:
            n = int(input("Enter a number: "))
            smallest_multiple = find_smallest_multiple(n)
            print(smallest_multiple)
        except ValueError:
            break

# Call the function to process test cases
process_test_cases()

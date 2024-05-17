def is_palindrome(n):
    return str(n) == str(n)[::-1]

def reverse_and_add(n):
    iterations = 0
    while not is_palindrome(n):
        reversed_n = int(str(n)[::-1])
        n += reversed_n
        iterations += 1
    return iterations, n

def main():
    test_cases = int(input("Enter the number of test cases: "))
    for _ in range(test_cases):
        number = int(input("Enter the number: "))
        iterations, palindrome = reverse_and_add(number)
        print(iterations, palindrome)

if __name__ == "__main__":
    main()

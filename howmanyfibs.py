def fibonacci(n):
    a, b = 0, 1
    fib_list = []
    while b < n:
        fib_list.append(b)
        a, b = b, a + b
    return fib_list

def count_fibonacci_in_range(f, s, fib_list):
    count = 0
    for num in fib_list:
        if f <= num < s:
            count += 1
    return count

fib_list = fibonacci(10**100)

while True:
    f, s = map(int, input("Enter two numbers (or 0 0 to exit): ").split())
    if f == 0 and s == 0:
        break
    count = count_fibonacci_in_range(f, s, fib_list)
    print(count)

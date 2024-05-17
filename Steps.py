from math import ceil, sqrt

def solve(x, y):
    # Calculate the difference between y and x
    diff = y - x

    # Calculate the minimum number of steps
    # We move 1 unit until we reach halfway, then we move 2 units
    steps = ceil(sqrt(diff))

    return steps

def main():
    cases = int(input("Enter the number of cases: "))
    results = []
    for _ in range(cases):
        x, y = map(int, input().split())
        results.append(solve(x, y))
    return results

if __name__ == "__main__":
    results = main()
    for result in results:
        print(result)

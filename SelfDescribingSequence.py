def find_golomb(n):
    golomb = [0] * (n + 1)
    golomb[1] = 1
    for i in range(2, n + 1):
        golomb[i] = 1 + golomb[i - golomb[golomb[i - 1]]]
    return golomb

def find_f(n):
    golomb_sequence = find_golomb(n) # Dynamically compute Golomb numbers up to n
    return golomb_sequence[n]

while True:
    n = int(input())
    if n == 0:
        break
    print(find_f(n))

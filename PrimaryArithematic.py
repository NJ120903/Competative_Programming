def binomialCoeff(n, k):
    if k > n:
        return 0
    res = 1
    for i in range(k):
        res *= (n - i)
        res //= (i + 1)
    return res

def main():
    while True:
        try:
            n, k = map(int, input("Enter n and k separated by a space (or press Enter to exit): ").split())
        except ValueError:
            break
        
        f = [0] * (n + 1)
        for i in range(n + 1):
            f[i] = binomialCoeff(n, i)

        if k < 0 or k > n:
            print("Coefficient is 0")
        else:
            print(f"Coefficient of x^{k} in (1 + x)^{n} is: {f[k]}")

if __name__ == "__main__":
    main()

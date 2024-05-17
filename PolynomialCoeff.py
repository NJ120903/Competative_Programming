import math

def main():
    f = [1] * 15
    for n in range(1, 15):
        f[n] = f[n - 1] * n
    
    while True:
        try:
            n, k = map(int, input("Enter n and k separated by a space (or press Enter to exit): ").split())
            if n == 0 and k == 0:
                break
            
            ans = f[n]
            m_input = input("Enter the values of m separated by spaces: ")
            if not m_input:
                raise EOFError
            
            m_values = list(map(int, m_input.split()))
            for m in m_values:
                for _ in range(k):
                    ans //= f[m]
            print(ans)
        
        except ValueError:
            print("Invalid input. Please enter integers.")
        except EOFError:
            print("Exiting.")
            break

if __name__ == "__main__":
    main()

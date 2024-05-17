def main():
    while True:
        try:
            n = int(input())
            if n == 1:
                print("Stan wins.")
                continue
            cont = 0
            while n > 1:
                cont += 1
                if cont % 2 == 1:
                    n = (n + 8) // 9
                else:
                    n = (n + 1) // 2
            if cont % 2 == 1:
                print("Stan wins.")
            else:
                print("Ollie wins.")
        except EOFError:
            break

if __name__ == "__main__":
    main()

def generate_table(num):
    t = [0, 2, 5, 13]  # Initial values
    for n in range(4, num + 1):
        t.append(2 * t[n - 1] + t[n - 2] + t[n - 3])
    return t

TABLE = generate_table(1000)

while True:
    line = input("Enter a number (or press Enter to exit): ")
    if not line:
        break
    try:
        index = int(line)
        if 0 <= index <= 1000:
            print(TABLE[index])
        else:
            print("Index out of range. Please enter a number between 0 and 1000.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

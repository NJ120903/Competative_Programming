def solve(s, text):
    arr = [
        [' - ', '   ', ' - ', ' - ', '   ', ' - ', ' - ', ' - ', ' - ', ' - '],
        ['| |', '  |', '  |', '  |', '| |', '|  ', '|  ', '  |', '| |', '| |'],
        ['   ', '   ', ' - ', ' - ', ' - ', ' - ', ' - ', '   ', ' - ', ' - '],
        ['| |', '  |', '|  ', '  |', '  |', '  |', '| |', '  |', '| |', '  |'],
        [' - ', '   ', ' - ', ' - ', '   ', ' - ', ' - ', '   ', ' - ', ' - ']
    ]
    text_len = len(text)
    for i in range(5):
        row = ''
        for j in range(text_len):
            cell = arr[i][int(text[j])]
            row += '{}{}{}'.format(cell[0], cell[1]*s, cell[2])
            if j != text_len - 1:
                row += ' ' * 2  # Modified to add two spaces between digits
        if i % 2 == 1:  # Only expand vertically for segments that should be
            for _ in range(s):
                print(row)
        else:
            print(row)

if __name__ == '__main__':
    arr = []
    while True:
        line = input().strip()
        if not line:
            continue  # Skip any empty lines
        if line == '0':
            break
        try:
            s, n = line.split()
            s = int(s)
            arr.append([s, n])
        except ValueError:
            print("Invalid input format. Please enter in the format: <scale> <number>")

    for i in range(len(arr)):
        solve(arr[i][0], arr[i][1])
        print('')

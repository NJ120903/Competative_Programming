adj = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def drawRectangle(x1, y1, x2, y2, colour):
    for i in range(y1, y2 + 1):
        for j in range(x1, x2 + 1):
            currentImage[i][j] = colour

def isValid(x, y):
    return 0 <= y < len(currentImage) and 0 <= x < len(currentImage[y])

def drawRegion(x, y):
    visited[y][x] = True
    currentImage[y][x] = colour
    for dx, dy in adj:
        x1, y1 = x + dx, y + dy
        if isValid(x1, y1) and not visited[y1][x1] and selectedColour == currentImage[y1][x1]:
            drawRegion(x1, y1)

while True:
    try:
        line = input()
    except EOFError:
        break
    if line == 'X':
        break

    command, *args = line.split()
    
    if command == 'I':  # Create a new image
        m, n = map(int, args)
        visited = [[False] * m for _ in range(n)]
        currentImage = [['O'] * m for _ in range(n)]
    
    elif command == 'C':  # Clear the image
        currentImage = [['O'] * len(currentImage[0]) for _ in range(len(currentImage))]
    
    elif command == 'L':  # Draw a single pixel
        x, y, colour = int(args[0]), int(args[1]), args[2]
        currentImage[y - 1][x - 1] = colour
    
    elif command == 'V':  # Draw a vertical segment
        x, y, y1, colour = int(args[0]), int(args[1]), int(args[2]), args[3]
        if y > y1:
            y, y1 = y1, y
        drawRectangle(x - 1, y - 1, x - 1, y1 - 1, colour)
    
    elif command == 'H':  # Draw a horizontal segment
        x, x1, y, colour = int(args[0]), int(args[1]), int(args[2]), args[3]
        if x > x1:
            x, x1 = x1, x
        drawRectangle(x - 1, y - 1, x1 - 1, y - 1, colour)
    
    elif command == 'K':  # Draw a rectangle
        x, y, x1, y1, colour = int(args[0]), int(args[1]), int(args[2]), int(args[3]), args[4]
        if x > x1:
            x, x1 = x1, x
        if y > y1:
            y, y1 = y1, y
        drawRectangle(x - 1, y - 1, x1 - 1, y1 - 1, colour)
    
    elif command == 'F':  # Fill region
        x, y, colour = int(args[0]), int(args[1]), args[2]
        selectedColour = currentImage[y - 1][x - 1]
        visited = [[False] * len(currentImage[0]) for _ in range(len(currentImage))]
        drawRegion(x - 1, y - 1)
    
    elif command == 'S':  # Print the image
        name = args[0]
        print(name)
        for row in currentImage:
            print(''.join(row))

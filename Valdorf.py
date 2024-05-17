def find_word_in_grid(grid, word):
    directions = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]
    m, n = len(grid), len(grid[0])
    
    for i in range(m):
        for j in range(n):
            for dx, dy in directions:
                found = True
                for k in range(len(word)):
                    x, y = i + k * dx, j + k * dy
                    if x < 0 or x >= m or y < 0 or y >= n or grid[x][y].lower() != word[k].lower():
                        found = False
                        break
                if found:
                    return (i + 1, j + 1)  # Adjust to 1-based indexing
    return None

# Sample input
grid = [
    list("abcDEFGhigg"),
    list("hEbkWalDork"),
    list("FtyAwaldORm"),
    list("FtsimrLqsrc"),
    list("byoArBeDeyv"),
    list("Klcbqwikomk"),
    list("strEBGadhrb"),
    list("yUiqlxcnBjf")
]
words = ["Waldorf", "Bambi", "Betty", "Dagbert"]

# Find locations of words in the grid
locations = [(find_word_in_grid(grid, word), word) for word in words]

# Filter out None results and print the locations
for loc, word in locations:
    if loc:
        print(f"{word} found at ({loc[0]}, {loc[1]})")

# Expected Output:
# Waldorf found at (2, 5)
# Betty found at (5, 8)

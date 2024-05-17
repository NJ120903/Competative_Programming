n = int(input())
for _ in range(n):
    d = int(input())
    m = int(input())
    c = [0] * m
    for i in range(m):
        c[i] = int(input())
    
    total = 0
    for i in range(1, d+1):
        if i % 7 == 6 or i % 7 == 0:  # Check if Saturday or Sunday
            continue
        for j in range(m):
            if i % c[j] == 0:  # Check if there's an event on this day
                total += 1
                break  # Stop checking for events once one is found
    
    print(total)

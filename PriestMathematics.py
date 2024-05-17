T = [0, 1]
opt = 2
for i in range(2, 10001):
    ans = 2 * T[1] + 2**(i - 1) - 1
    for j in range(opt, i):
        cur = 2 * T[j] + 2**(i - j) - 1
        if cur < ans:
            ans = cur
            opt = j
        else:
            break
    T.append(ans)

while True:
    try:
        line = input()
        print(T[int(line)])
    except EOFError:
        break

def readnum():
    line = input()
    if not line:
        return None, None
    return [int(x) for x in line.split()]

def num_expressions(pairs, depth, mem):
    if (pairs, depth) in mem:
        return mem[(pairs, depth)]
    if pairs == 0 or depth == 1:
        mem[(pairs, depth)] = 1
        return 1
    total = 0
    for i in range(pairs):
        total += num_expressions(i, depth - 1, mem) * num_expressions(pairs - 1 - i, depth, mem)
    mem[(pairs, depth)] = total
    return total

if __name__ == "__main__":
    mem = {}
    while True:
        n, d = readnum()
        if not n:
            break
        nexp = num_expressions(n // 2, d, mem) - num_expressions(n // 2, d - 1, mem)
        print(nexp)

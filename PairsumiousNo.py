def find_integers(n, sums):
    # Sort the pairwise sums
    sums.sort()

    # Create a dictionary to store the indices of each sum
    indices = {}
    for i, s in enumerate(sums):
        indices.setdefault(s, []).append(i)

    # Initialize variables
    used = 0
    flag = False
    for i in range(2, len(sums)):
        # A[1] + A[2] = sums[i]
        if (sums[0] + sums[1] + sums[i]) % 2 != 0:
            continue
        tmp = (sums[0] + sums[1] + sums[i]) // 2
        A = [0] * n
        A[0] = tmp - sums[i]
        A[1] = tmp - sums[1]
        A[2] = tmp - sums[0]
        used = 1 << i
        idx = 2
        used |= 1
        used |= 2
        for j in range(3, n):
            while used & (1 << idx):
                idx += 1
            A[j] = sums[indices[sums[idx]][0]] - A[0]
            # Delete A[j] + A[0-(j-1)]
            for k in range(j):
                tmp = A[j] + A[k]
                if tmp not in indices:
                    break
                ok = False
                for jt in indices[tmp]:
                    if not (used & (1 << jt)):
                        used |= 1 << jt
                        ok = True
                        break
                if not ok:
                    break
            else:
                continue
            break
        else:
            # Output answer
            flag = True
            result = [str(x) for x in A]
            return " ".join(result)
    
    if not flag:
        return "Impossible"

def process_test_cases():
    while True:
        try:
            line = input().strip() # Remove leading/trailing whitespace
            if not line:
                break
            # Extract integers from the line
            numbers = [int(x) for x in line.split()]
            n, sums = numbers[0], numbers[1:]
            integers = find_integers(n, sums)
            print(integers)
        except EOFError:
            break

process_test_cases()

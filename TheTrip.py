def solve(arr):
    avg = sum(arr) / len(arr)
    pos_diff, neg_diff = 0.0, 0.0
    
    for num in arr:
        val = int((num - avg) * 100.0) / 100.0  # Round to the nearest cent
        if val < 0:
            neg_diff += val
        else:
            pos_diff += val
    
    neg_diff *= -1  # Make neg_diff positive since it's a sum of negative values
    res = max(neg_diff, pos_diff)  # The result is the maximum of positive and negative diffs
    return '${0:.2f}'.format(res)

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    
    while idx < len(data):
        N = int(data[idx])
        idx += 1
        
        if N == 0:
            break
        
        arr = []
        for _ in range(N):
            arr.append(float(data[idx]))
            idx += 1
        
        print(solve(arr))

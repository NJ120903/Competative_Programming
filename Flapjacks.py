import sys
from copy import copy

def load_num():
    line = sys.stdin.readline()
    if line == '' or line == '\n':
        return None

    return list(map(int, line.rstrip().split()))

def find_pos(lst, element):
    for i in range(len(lst)):
        if lst[i] == element:
            return i
    return None

def iflip(stack, pos):

    if pos >len(stack) or pos <1:
        raise ValueError

    for i, j in zip(range(pos-1, len(stack)), range(len(stack)-1, pos-1, -1)):
        if i>=j:
            break
        stack[i], stack[j] = stack[j], stack[i]

def flip_sort(stack):
    flips = []
    sstack = sorted(stack, reverse = True)
    stack = list(stack[::-1])

    for i in range(len(stack)-1):
        if stack[i] == sstack[i]:
            continue

        pos = find_pos(stack, sstack[i])
        if pos != len(stack)-1:
            flips.append(pos+1)
            iflip(stack, pos+1)
        flips.append(i+1)
        iflip(stack, i+1)
   
    return flips

if __name__ == '__main__':

    while True:
        stack = load_num()
        if not stack:
            break
       
        print(" ".join(map(str, stack)))
        solution = flip_sort(stack)
        
        if solution:
            print(" ".join(map(str, solution+[0])))
        else:
            print(0)

    exit(0)
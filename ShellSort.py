import sys

def load_num():
    line = sys.stdin.readline()
    return int(line.rstrip())

def load_case():
    nturtles = load_num()
    
    unordered = []
    ordered = []

    for n in range(nturtles):
        unordered.append(sys.stdin.readline().rstrip())

    for n in range(nturtles):
        ordered.append(sys.stdin.readline().rstrip())

    return unordered, ordered

def shell_short(unordered, ordered):

    unordered = unordered[::-1]
    ordered = ordered[::-1]
    names = {}

    for i, name in enumerate(ordered):
        names[name] = i

    stack = [names[n] for n in unordered] 

    reorder = []
    for i in range(len(stack)):
        if stack[i] != i-len(reorder):
            reorder.append(stack[i])

    return [ordered[n] for n in sorted(reorder)]

if __name__ == '__main__':

    ncases = load_num()

    for c in range(ncases):
        unordered, ordered = load_case()
        for name in shell_short(unordered, ordered):
            print(name)
        else:
            print('')
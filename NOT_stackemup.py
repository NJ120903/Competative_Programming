import sys

def main():
    s1 = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    s2 = ["Clubs", "Diamonds", "Hearts", "Spades"]
    T = int(input())
    first = True
    for _ in range(T):
        N = int(input())
        p = []
        for _ in range(N):
            p.append(list(map(int, input().split())))
        for j in range(52):
            p[-1][j] -= 1
        cur = list(range(52))
        while True:
            try:
                line = input().strip()
                if not line:
                    break
                K = int(line) - 1
            except EOFError:
                break
            nxt = [0] * 52
            for i in range(52):
                nxt[i] = cur[p[K][i]]
            cur = nxt
        if not first:
            print()
        first = False
        for i in range(52):
            print("{} of {}".format(s1[cur[i] % 13], s2[cur[i] // 13]))

if __name__ == "__main__":
    main()

class Board:
    def __init__(self, contestant):
        self.contestant = contestant
        self.nproblem = 0
        self.problem = [0] * 10
        self.penalty = [0] * 10
        self.time = 0

    def calc_time(self):
        for i in range(1, 10):
            if self.problem[i] == 1:
                self.time += self.penalty[i]

def judge(b, problem, time, L):
    if b.problem[problem] == 1:
        return
    if L == 'C':
        b.nproblem += 1
        b.problem[problem] = 1
        b.penalty[problem] += time
    elif L == 'I':
        b.penalty[problem] += 20

def main():
    T = int(input())
    input()
    for t in range(1, T + 1):
        index = [-1] * 101
        v = []
        while True:
            try:
                s = input()
                if not s:
                    break
                contestant, problem, time, L = map(str, s.split())
                contestant = int(contestant)
                problem = int(problem)
                time = int(time)
                if index[contestant] == -1:
                    v.append(Board(contestant))
                    index[contestant] = len(v) - 1
                judge(v[index[contestant]], problem, time, L)
            except EOFError:
                break
        for board in v:
            board.calc_time()
        v.sort(key=lambda x: (-x.nproblem, x.time, x.contestant))
        for board in v:
            print(board.contestant, board.nproblem, board.time)
        if t < T:
            print()

if __name__ == "__main__":
    main()

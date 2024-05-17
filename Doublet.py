from collections import deque

def find_doublets(dictionary, word1, word2):
    queue = deque([(word1, [word1])])
    while queue:
        current, path = queue.popleft()
        if current == word2:
            return '\n'.join(path)
        for word in dictionary:
            if len(word) == len(current) and sum(c1 != c2 for c1, c2 in zip(word, current)) == 1:
                queue.append((word, path + [word]))
    return 'No solution'

def main():
    dictionary = set()
    while True:
        word = input()
        if not word:
            break
        dictionary.add(word)
    while True:
        try:
            line = input().split()
            if not line:
                break
            word1, word2 = line
            print(find_doublets(dictionary, word1, word2))
            print()
        except EOFError:
            break

if __name__ == "__main__":
    main()

import sys

def main():
    T = int(input())  # Read number of test cases
    ending_separator = ""

    for _ in range(T):
        n = int(input())  # Number of candidates
        names = [input().strip() for _ in range(n)]
        
        # Skip the empty line between candidate names and ratings
        sys.stdin.readline()
        
        ratings = []
        while True:
            temp = input().strip()
            if temp == "":
                break
            order = [int(x) - 1 for x in temp.split()]
            ratings.append(order)
            if sys.stdin.isatty() and not temp:
                break

        num_ratings = len(ratings)
        pos_in_ratings = [0] * num_ratings
        eliminated = [False] * n
        count = [0] * n

        # Initial count of first-choice votes
        for order in ratings:
            count[order[0]] += 1

        while True:
            highest = max(count)
            lowest = min(count)

            if highest * 2 > num_ratings or highest == lowest:
                break

            for i in range(n):
                if count[i] == lowest:
                    eliminated[i] = True
                    count[i] = 0

            for i in range(num_ratings):
                while eliminated[ratings[i][pos_in_ratings[i]]]:
                    pos_in_ratings[i] += 1
                count[ratings[i][pos_in_ratings[i]]] += 1

        print(ending_separator, end="")
        ending_separator = "\n"

        for i in range(n):
            if count[i] == highest and not eliminated[i]:
                print(names[i])

if __name__ == "__main__":
    main()

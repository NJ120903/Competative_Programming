from sys import stdin
from collections import Counter

CATEGORIES = 13

# IO Functions (read cases on stdin)
def readnum():
    return list(map(int, stdin.readline().split()))

def readgame():
    return [readnum() for _ in range(13)]

# Dice rating functions
def ones(dices):
    return sum(d for d in dices if d == 1)

def twos(dices):
    return sum(d for d in dices if d == 2)

# Define similar functions for threes, fours, fives, and sixes...

# Dictionary mapping category names to their corresponding functions
RATE_FUNCS = {
    'ones': ones,
    'twos': twos,
    # Add similar mappings for threes, fours, fives, and sixes...
}

# Define the other rating functions like three_kind, four_kind, etc...

# Build a table with the score for all the categories for each round
def build_score_table(game):
    return [[func(round) for func in RATE_FUNCS.values()] for round in game]

# Recursive function to find the best score for each round
def MaxScore(round, free_cat, prev6score, mem, score_table):
    if round == 13:
        return 0, 0, 0
    try:
        return mem[round, tuple(free_cat)]
    except KeyError:
        pass
    scores = []
    for cat, free in enumerate(free_cat):
        if not free:
            continue
        cat_score = score_table[round][cat]
        current6score = prev6score + cat_score if cat < 6 else prev6score
        free_cat[cat] = False
        rest_score, rest6score, _ = MaxScore(round + 1, free_cat, current6score, mem, score_table)
        free_cat[cat] = True
        fullscore = cat_score + rest_score
        full6score = current6score + rest6score
        bonus = 35 if full6score >= 63 else 0
        scores.append((fullscore + bonus, fullscore, full6score - prev6score, cat))
    _, bestscore, best6score, cat = max(scores)
    mem[(round, tuple(free_cat))] = (bestscore, best6score, cat)
    return (bestscore, best6score, cat)

# Find the best score for the entire game
def find_best_score(game):
    score_table = build_score_table(game)
    mem = {}
    total_score, first6score, first_cat = MaxScore(0, [True] * CATEGORIES, 0, mem, score_table)
    bonus = 35 if first6score >= 63 else 0
    score = []
    cat_free = [True] * CATEGORIES
    while len(score) < 13:
        best_score, first6score, cat = mem[(len(score), tuple(cat_free))]
        cat_free[cat] = False
        score.append((cat, score_table[len(score)][cat]))
    score = [value for cat, value in sorted(score)]
    return score, bonus, total_score + bonus

if __name__ == '__main__':
    while True:
        game = readgame()
        if len(game[0]) == 0:
            break
        score, bonus, total = find_best_score(game)
        print(" ".join(map(str, score)), bonus, total)

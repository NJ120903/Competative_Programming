def handle_straight(board, x, y, target1, target2):
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        while 0 <= nx < 8 and 0 <= ny < 8 and board[ny][nx] == '.':
            nx += dx
            ny += dy
        if 0 <= nx < 8 and 0 <= ny < 8 and (board[ny][nx] == target1 or board[ny][nx] == target2):
            return True
    return False

def handle_diagonal(board, x, y, target1, target2):
    for dx, dy in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
        nx, ny = x + dx, y + dy
        while 0 <= nx < 8 and 0 <= ny < 8 and board[ny][nx] == '.':
            nx += dx
            ny += dy
        if 0 <= nx < 8 and 0 <= ny < 8 and (board[ny][nx] == target1 or board[ny][nx] == target2):
            return True
    return False

def handle_knight(board, x, y, target):
    for dx, dy in [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 8 and 0 <= ny < 8 and board[ny][nx] == target:
            return True
    return False

def handle_pawn(board, x, y, target, y_change):
    for dx in [-1, 1]:
        nx = x + dx
        ny = y + y_change
        if 0 <= nx < 8 and 0 <= ny < 8 and board[ny][nx] == target:
            return True
    return False

def main():
    t = 1
    while True:
        try:
            board = [input() for _ in range(8)]
        except EOFError:
            break

        white_pos = black_pos = None
        for i in range(8):
            if 'k' in board[i]:
                black_pos = (board[i].index('k'), i)
            if 'K' in board[i]:
                white_pos = (board[i].index('K'), i)
        
        if white_pos is None or black_pos is None:
            break
        
        print(f"Game #{t}: ", end='')

        if handle_pawn(board, white_pos[0], white_pos[1], 'p', -1):
            print("white king is in check.")
        elif handle_pawn(board, black_pos[0], black_pos[1], 'P', 1):
            print("black king is in check.")
        elif handle_knight(board, white_pos[0], white_pos[1], 'n'):
            print("white king is in check.")
        elif handle_knight(board, black_pos[0], black_pos[1], 'N'):
            print("black king is in check.")
        elif handle_straight(board, white_pos[0], white_pos[1], 'r', 'q'):
            print("white king is in check.")
        elif handle_straight(board, black_pos[0], black_pos[1], 'R', 'Q'):
            print("black king is in check.")
        elif handle_diagonal(board, white_pos[0], white_pos[1], 'b', 'q'):
            print("white king is in check.")
        elif handle_diagonal(board, black_pos[0], black_pos[1], 'B', 'Q'):
            print("black king is in check.")
        else:
            print("no king is in check.")

        t += 1

if __name__ == "__main__":
    main()

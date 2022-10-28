def get_total_board(board) -> int:
    total = 0
    for b in board:
        for k, v in b.items():
            if v == 0:
                total += k
    return total

def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()
    bingos =[int(x) for x in content[0].strip().split(",")]
    
    # [
    # dict(38 80 23 60 82)
    # dict(25 35 28 47 39)
    # dict(40  0 30 48 76)
    # dict(32 41 49 69  4)
    # dict(13 42 89 20 12)
    # ]
    boards = []
    line = 2
    while line < len(content):
        if len(content[line]) < 2:
            continue
        curr_board = []
        for _ in range(5):
            curr_board.append({int(x):0 for x in content[line].strip().split()})
            line += 1
        line += 1
        boards.append(curr_board)

    last_board: tuple(int, list) = None
    winning_boards = set()
    for b in bingos:
        for board in boards:
            for i, row in enumerate(board):
                if str(board) not in winning_boards:
                    if b in row:
                        row[b] = 1
                    if sum(row.values()) == 5:
                        winning_boards.add(str(board))
                        last_board = (b, board)
                    cols = 0
                    for x in board:
                        row = list(x.keys())
                        if x[row[i]] == 1:
                            cols += 1
                    if cols == 5:
                        winning_boards.add(str(board))
                        last_board = (b, board)

    print(last_board[0] * get_total_board(last_board[1]))

if __name__ == "__main__":
    raise SystemExit(main())


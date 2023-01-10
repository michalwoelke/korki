from utils import read_file


def main():
    boards_str = read_file('Dane_2203/szachy.txt').strip().split('\n\n')
    boards = []  # list(map(to_two_dim, boards_str))
    for board_str in boards_str:
        boards.append(to_two_dim(board_str))

    zad1(boards)
    zad2(boards)


def to_two_dim(board: str):
    rows = board.split('\n')
    two_dim_arr = []
    for row in rows:
        row_arr = []
        for char in row:
            row_arr.append(char)
        two_dim_arr.append(row_arr)
    return two_dim_arr


def print_2d_arr(arr):
    for row in arr:
        for el in row:
            print(el, end="")
        print()


# === PODPUNKT 1
def zad1(boards):
    boards_with_empty_columns = 0
    empty_columns_in_board = []
    for board in boards:
        if count_empty_columns(board) > 0:
            boards_with_empty_columns += 1
            empty_columns_in_board.append(count_empty_columns(board))
    print('zad 1.1: ', boards_with_empty_columns, max(empty_columns_in_board))


def count_empty_columns(board: list):
    result = 0
    for column in range(8):
        is_empty = True
        for row in range(8):
            if board[row][column] != '.':
                is_empty = False
                break
        if is_empty:
            result += 1
    return result


# === PODPUNKT 2
def zad2(boards):
    equal_boards = 0
    pieces_on_boards = []
    for board in boards:
        white_pieces = []
        black_pieces = []
        for row in board:
            for char in row:
                if char != '.':
                    if char.islower():
                        black_pieces.append(char.upper())
                    else:
                        white_pieces.append(char)
        if sorted(white_pieces) == sorted(black_pieces):
            equal_boards += 1
            pieces_on_boards.append(2*len(white_pieces))
    print("zad 1.2: ", equal_boards, min(pieces_on_boards))


if __name__ == '__main__':
    main()

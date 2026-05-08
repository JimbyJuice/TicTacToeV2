KNOT = "O"
CROSS = "X"
PLAYER1 = 1
PLAYER2 = -1

playerToMove = {PLAYER1: KNOT, PLAYER2: CROSS}

def get_player_action() -> tuple:
    return tuple(map(int, input("Enter row col: ").split()))

def print_board(board: list[list[chr]]):
    for i in range(len(board)):
        print(' ' + " | ".join(board[i]) + ' ')
        if i < 2:
            print("---+---+---")

def update_board(move, board, currPlayer):
    board[move[0]][move[1]] = playerToMove[currPlayer]
    return board

def game_finished():
    pass

def main():
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    currPlayer = PLAYER1
    print_board(board)
    while (1):
        move = get_player_action()
        update_board(move, board, currPlayer)
        print_board(board)
        currPlayer = -currPlayer
    # while not game_finished():
    #     print_board(board)
    #     get_player_action()
    #     update_board()

if __name__ == "__main__":
    main()
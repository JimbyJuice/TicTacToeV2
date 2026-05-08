from collections import deque

KNOT = "O"
CROSS = "X"
PLAYER1 = 1
PLAYER2 = -1
UNSET = ' '

playerToMove = {PLAYER1: KNOT, PLAYER2: CROSS}

# hot seat feature, show which cells are expiring
# choose what char for each player
# solve board feat (when game ends)

def get_player_action(board: list[list[chr]]) -> tuple:
    while True:
        try:
            choice = tuple(map(int, input("Enter row col: ").split()))
            
        except ValueError:
            print("Please enter valid input!")
            continue

        if len(choice) != 2:
            print("Please enter as row col")
            continue
        
        row = choice[0]
        col = choice[1]
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Out of bounds!")
            continue
        
        if board[row][col] != UNSET:
            print("Choice is occupied!")
            continue
        
        return choice

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
        [UNSET, UNSET, UNSET],
        [UNSET, UNSET, UNSET],
        [UNSET, UNSET, UNSET]
    ]
    currPlayer = PLAYER1
    queue = deque()
    
    print_board(board)
    while (1):
        move = get_player_action(board)
        queue.append(move)
        if len(queue) == 6:
            expiredMove = queue.popleft()
            board[expiredMove[0]][expiredMove[1]] = UNSET
        update_board(move, board, currPlayer)
        print_board(board)
        currPlayer = -currPlayer
    # while not game_finished():
    #     print_board(board)
    #     get_player_action()
    #     update_board()

if __name__ == "__main__":
    main()
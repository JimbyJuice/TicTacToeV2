import tkinter as tk
from game import TicTacToeGame, PLAYER1, playerToMove

class TicTacToeUI:
    def __init__(self):
        self.game = TicTacToeGame()
        
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.resizable(False, False)
        
        self.statusLabel = tk.Label(self.window, text="Player 1's turn (O)", font=("Arial", 14))
        self.statusLabel.grid(row=0, column=0, columnspan=3, pady=10)
        
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()
        
        resetBtn = tk.Button(self.window, text="Restart", command=self._reset)
        resetBtn.grid(row=4, column=0, columnspan=3, pady=10)
        
    def create_board(self):
        for row in range(3):
            for col in range(3):
                btn = tk.Button(self.window, text=" ", width=8, height=4, font=("Arial", 20), command=lambda r=row, c=col: self._on_click(r, c))
                btn.grid(row=row+1, column=col, padx=4, pady=4)
                self.buttons[row][col] = btn
                
    def _on_click(self, row, col):
        if not self.game.make_move(row, col):
            return
        
        self.buttons[row][col].config(text=self.game.get_symbol(row, col))
        
        if self.game.expiredCell is not None:
            r, c = self.game.expiredCell
            self.buttons[r][c].config(text=" ")
            
        winner = self.game.check_winner()
        if winner is not None:
            self.statusLabel.config(text=f"*** Player {winner} is the winner! ***")
            for row in self.buttons:
                for btn in row:
                    btn.config(state=tk.DISABLED)
        else:
            current = self.game.currentPlayer
            self.statusLabel.config(text=f"Player {current}'s turn ({playerToMove[current]})")
    
    def run(self):
        self.window.mainloop()
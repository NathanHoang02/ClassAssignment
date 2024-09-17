# Text based tic-tac-toe:
import numpy as np

class Board:
    def __init__(self):
        
    def check_winer(self) -> None|str:
        
    def check_tie(self) -> bool:
        
    def mark_move(self, player:str, x:int, y:int):
        
    def print_board(self):


def computer_move(board: Board) -> tuple[int, int]:

# Input 
def get_user_input(msg: str) -> tuple[int, int]:
    user_input = input(msg)


def run_game():
    board = Board()
    end_game = False
    players = ['user', 'computer']
    next = 0 if np.random.rand() < 0.5 else 1
    while not end_game:
        board.print_board()
        player = players[next]
        if player == 'user':
            x, y = get_user_input()
            board.mark_move('user', x, y)
        else:
             x, y = computer_move(board)
             board.mark_move('computer', x, y)
             print('Computer move', x, y)
        winer = board.check_winer()
        tie = board.check_tie()

        if winer is not None:
             print(f'Game ended. Winer is {winer}')
             end_game = True
        elif tie:
             print('Game ends with a tie!')
             end_game = True
        else:
            next = (next + 1) % 2

if __name__ is '__main__':
     run_game()

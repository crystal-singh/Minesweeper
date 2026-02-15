from minesweeper import Minesweeper

class Game:
    def __init__(self, minesweeper:Minesweeper):
        self.minesweeper = minesweeper # refers to superclass
        self.game_over = False # determines if game is over

    def reveal(self, row, col):
        # tries to reveal cell; bomb - game over
        if not self.minesweeper.reveal_cell(row, col):
            self.game_over = True
            self.minesweeper.display()
            print('You hit a bomb! Game over :(')
            self.minesweeper.reveal_full_board()
        # if the player reveals all non-bomb cells; game ends
        elif self.minesweeper.is_winner():
            self.game_over = True
            self.minesweeper.display()
            print('Congratulations! You won :)')
            self.minesweeper.reveal_full_board()
        # game continuing by revealing current cell
        else:
            print(f'Cell ({row}, {col}) revealed.')
            self.game_over = False
            self.minesweeper.display()
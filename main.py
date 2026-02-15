from minesweeper import Minesweeper
from gameplay import Game
from user import User

def main():
    print('Welcome to Minesweeper!') # introductory message

    # sets up the grid with player inputs
    h = User.get_input("Enter the grid height: ", 1)
    w = User.get_input("Enter the grid width: ", 1)
    bomb_density = User.get_float_input("Enter the bomb density (in terms of percentage): ", 0.1, 0.9)

    # sets up the game
    minesweeper = Minesweeper(h, w, bomb_density)
    game = Game(minesweeper)

    minesweeper.display()

    # keeps the game running until it's over
    while not game.game_over:
        print("\nEnter your move:")
        row = User.get_input(f"Enter row (0 to {h - 1}): ", 0, h - 1)
        col = User.get_input(f"Enter column (0 to {w - 1}): ", 0, w - 1)
        game.reveal(row, col)

    print("Thanks for playing!")


if __name__ == '__main__':
    main()
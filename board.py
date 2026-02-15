class Board:
    @staticmethod
    def display(grid):
        print('\n'.join([' '.join(row) for row in grid]))
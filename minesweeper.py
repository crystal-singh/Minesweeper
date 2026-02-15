import random

class Minesweeper:
    def __init__(self, h, w, b_p = 0.15):
        self.height = h
        self.width = w
        self.bombs = int(w * h * b_p) # calculates the number of bombs
        self.visible = [['-' for x in range(w)] for y in range(h)] # grid visible to player
        self.grid = [[' ' for x in range(w)] for y in range(h)] # grid with bombs and numbers
        self.bomb_pos = self._place_bombs()
        self._calculate_nums()

    def _place_bombs(self):
        bomb_pos = set()
        while len(bomb_pos) < self.bombs:
            position = random.randint(0, self.width * self.height -1)
            bomb_pos.add(position)
        # converts indexes to rows/cols and places a bomb "B" there
        for position in bomb_pos:
            row, col = divmod(position, self.width)
            self.grid[row][col] = 'B'
        return bomb_pos
    
    def _calculate_nums(self):
        directions = [(0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1)] # 8 surrounding cells
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] == 'B':
                    continue # skips bomb cells
                bomb_count = 0
                # checks all neighboring cells for bombs
                for d_row, d_col in directions:
                    n_row, n_col = row + d_row, col + d_col
                    if 0 <= n_row < self.height and 0 <= n_col < self.width and self.grid[n_row][n_col] == 'B':
                        bomb_count += 1
                # updates the bomb count on the grid
                if bomb_count > 0:
                    self.grid[row][col] = str(bomb_count)
                    

    def _reveal_empty_cells(self, row, col):
        directions = [(0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1)]
        stack = [(row, col)]
        while stack:
            r, c = stack.pop()
            if not (0 <= r < self.height and 0 <= c < self.width):
                continue # skip if out of bounds
            self.visible[r][c] = self.grid[r][c] # current cell
            # adds its neighbors to stack if cell is empty
            if self.grid[r][c] == ' ':
                for d_row, d_col in directions:
                    stack.append((r + d_row, c + d_col))

    def reveal_cell(self, row, col):
        # ends game if player lands on a bomb
        if self.grid[row][col] == 'B':
            print(f'Bam! You landed on a bomb! You lost!')
            return False
        # reveals empty cells recursively or numbered cells
        if self.grid[row][col] == ' ':
            self._reveal_empty_cells(row, col)
        else:
            self.visible[row][col] = self.grid[row][col]
        print(f'Cell ({row}, {col}) revealed.')
        return True

    def display(self):
        # reveals current board
        print(f'\nCurrent Board:')
        for row in self.visible:
            print(' '.join(row))

    def is_winner(self):
        # true if player wins; otherwise they lose
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] != 'B' and self.visible[row][col] == '-':
                    return False
        return True
    
    def reveal_full_board(self):
        # reveals final board after the game
        print("\nFinal Board:")
        for row in self.grid:
            print(' '.join(row))

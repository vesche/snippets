vline = '│'
hline = '─'

tlcorner = '┌'
trcorner = '┐'
blcorner = '└'
brcorner = '┘'

cross = '┼'
tcross = '┬'
lcross = '├'
rcross = '┤'
bcross = '┴'

block = '█'
lblock = '▌'
rblock = '▐'

edge = hline * 4
tile_blank = ' ' * 4
tile_full = ' ' + block*2 + ' '


class Grid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.board = [0 for _ in range(x*y)]
        self.top_row = tlcorner + (edge + tcross) * (self.x-1) + edge + trcorner
        self.mid_row = lcross + (edge + cross) * (self.x-1) + edge + rcross
        self.bot_row = blcorner + (edge + bcross) * (self.x-1) + edge + brcorner
        self.hold_array = list()

    def _get_pos(self, x, y):
        return y * self.y + x

    def get_tile(self, x, y):
        if self.board[self._get_pos(x, y)]:
            return tile_full
        return tile_blank

    def flip_tile(self, x, y):
        self.board[self._get_pos(x, y)] = 1 - self.board[self._get_pos(x, y)]

    def array(self, x, y, piece):
        for i in self.hold_array:
            self.board[i] = 0

        self.hold_array = list()
        for i in range(1, 26):
            if piece[i-1]:
                self.hold_array.append(self._get_pos(x, y))
            if i % 5 == 0:
                y += 1
                x -= 4
            else:
                x += 1
        
        for i in self.hold_array:
            self.board[i] = 1

    #def set_array(self, array):
    #    for i in array:
    #        self.board[i] = 1

    def display(self):
        # top
        print(self.top_row)
        # mid
        for y in range(self.y):
            tiles = [self.get_tile(x, y) for x in range(self.x)]
            print(vline + vline.join(tiles) + vline)
            if y != self.y-1:
                print(self.mid_row)
        # bot
        print(self.bot_row)

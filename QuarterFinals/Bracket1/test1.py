class ChessPiece:
    def __init__(self, color, symbol):
        self.color = color
        self.symbol = symbol

    def move(self):
        pass

class Pawn(ChessPiece):
    def move(self):
        return "Forward 1 square"

class Rook(ChessPiece):
    def move(self):
        return "Horizontally or vertically"

class Bishop(ChessPiece):
    def move(self):
        return "Diagonally"

class ChessGame:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]

    def place_piece(self, piece, row, col):
        self.board[row][col] = piece

    def move_piece(self, from_row, from_col, to_row, to_col):
        piece = self.board[from_row][from_col]
        if piece:
            self.board[from_row][from_col] = None
            self.board[to_row][to_col] = piece
            return f"{piece.color} {piece.symbol} moves {piece.move()} from ({from_row}, {from_col}) to ({to_row}, {to_col})"
        else:
            return "No piece at the specified position"


pawn1 = Pawn(color="White", symbol="P")
rook1 = Rook(color="Black", symbol="R")

game = ChessGame()
game.place_piece(pawn1, 1, 2)
game.place_piece(rook1, 7, 7)

print(game.move_piece(1, 2, 2, 2))
print(game.move_piece(7, 7, 5, 7))

"""#
What type of piece is present at (7,7) ?
"""



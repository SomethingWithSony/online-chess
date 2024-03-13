
class ChessBoard:
  """
  This class handles the state of the board, piece movement, and game logic.
  """
  def __init__(self):
    # The board ias an 8x8 matrix , each piece has 2 characters
    # The first character represents the piece color
    # The second character represents the piece type : "p" , "b", "r", "k"(King) or "n"(Knight)
    self.board = [
      ["br","bn","bb","bq","bk","bb","bn","br"],
      ["bp","bp","bp","bp","bp","bp","bp","bp"],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      ["wp","wp","wp","wp","wp","wp","wp","wp"],
      ["wr","wn","wb","wq","wk","wb","wn","wr"],
    ]
    self.white_turn = True
    self.moveLog = [] # Save moves

  def make_move(self,move):
    

    if self.white_turn and "w" in move.piece_moved:
      self.board[move.start_row][move.start_col] = 0
      self.board[move.end_row][move.end_col] = move.piece_moved
      self.white_turn = not self.white_turn
    elif not self.white_turn  and "b" in move.piece_moved:
      self.board[move.start_row][move.start_col] = 0
      self.board[move.end_row][move.end_col] = move.piece_moved
      self.white_turn = not self.white_turn

    
      
    


# Start by decomposing needs of the class
class Move:

  # In ches rows are called ranks and cols are called files
  # This will be used to store player movements 
  ranks_to_rows = {"8": 0, "7": 1, "6": 2, "5": 3, "4": 4, "3": 5, "2": 6, "1": 7 }
  rows_to_ranks = {ro: ra for ra, ro in ranks_to_rows.items()}

  files_to_cols = {"a": 0, "b" : 1, "c": 2, "d": 3, "e":  4, "f": 5, "g": 6 , "h": 7}
  cols_to_files = {f: c for c, f in files_to_cols.items()}

  def __init__(self,start_square,end_square, board):
    self.start_row = start_square[0]
    self.start_col = start_square[1]

    self.end_row = end_square[0]
    self.end_col = end_square[1]

    self.piece_moved = board[self.start_row][self.start_col]
    self.piece_captured = board[self.end_row][self.end_col]

  def get_chess_notation(self):
    # Study real chess notation and replicate it 
    return self.get_rank_file(self.start_row,self.start_col) + self.get_rank_file(self.end_row,self.end_col)
  
  def get_rank_file(self, row, col):
    return self.cols_to_files[col] + self.rows_to_ranks[row] 



    

    


# Game Logic
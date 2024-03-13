
class ChessBoard():
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
    self.moveLog = [] # Interesting

  class Move():
    def __init__(self):
      self.selected = False
      self.position = []
      self.piece = ""
      self.end_position = []

  # Check if movement is valid
  # If valid update start position to 0 and put piece in end_position
  # Validations 
  # Check piece movement pattern
      

    

    
  
class Pawm():
  pass

class Rook():
  pass

class Knight():
  pass

class Queen():
  pass

class King():
  pass

class Bishop():
  pass


# Game Logic
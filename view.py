import pygame as pygame
from model import ChessBoard, Move
import math

WIDTH = HEIGHT = 400
DIMENSION = 8
SQUARE_SIZE = WIDTH / DIMENSION
IMAGES = {}

# Initializes global dictionary of images. This will be called once upon inicialization
def load_images():
  pieces = ["wp" , "bp", "wr", "br" ,"wn","bn", "wb", "bb", "wk", "bk", "wq", "bq"]
  for piece in pieces:
    IMAGES[piece] = pygame.transform.scale(pygame.image.load("images/" + piece + ".png"), (SQUARE_SIZE, SQUARE_SIZE))
    # Note: images can be called by using <IMAGES["wp"]>
  
# This class is responsible for rendering the graphical representation of the chessboard.

# Handles user input & graphics
def main():
  pygame.init()
  screen = pygame.display.set_mode((WIDTH,HEIGHT))
  screen.fill(pygame.Color("white"))
  load_images()
  
  game_state = ChessBoard()
  clock = pygame.time.Clock()

  player_position = [] # Stores the initial and the final position 
  player_click = () # Stores de col and row when a player clicks a square
  same_play = True 

  framerate = 60
  running = True

  while running:
    # Check for pygame events
    for event in pygame.event.get():
      # Quit if X is pressed
      if event.type == pygame.QUIT:
        running = False

      if len(player_position) == 2:
            move = Move(player_position[0],player_position[1],game_state.board)
            game_state.make_move(move)
            player_position = []

      if event.type == pygame.MOUSEBUTTONDOWN:
        col, row = pygame.mouse.get_pos()
        row = math.ceil(row / 50) - 1
        col = math.ceil(col / 50) - 1

        board_info = game_state.board[row][col]
        player_click = (row,col)

        if not player_position: # No Move 
          if board_info != 0:
            player_position.append(player_click)
        else:
         
          if player_position[0] == player_click:
            player_position = [] # Resets position if same pawn is clicked
          else:
            player_position.append(player_click)
          

        
        print(player_position)
      
      elif event.type == pygame.MOUSEBUTTONUP:
        col, row = pygame.mouse.get_pos()
        row = math.ceil(row / 50) - 1
        col = math.ceil(col / 50) - 1

        board_info = game_state.board[row][col]
        player_click = (row,col)

        # Lets say if its white turn and gets on a white piece
        if not player_position:
          pass # Do nothing
        else: 
            if board_info == 0:
              player_position.append(player_click)
          

        player_click = ()
        print(player_position)
     
      
      """
      Chess player clicks on a piece and its the first click
      Chess clicks on a piece and its the second click
      
      """
       
    draw_states(screen,game_state)

    clock.tick(framerate)
    pygame.display.flip()


"""
Draws squares on the board
"""
def draw_board(screen):
  colors = [pygame.Color("#ebecd0"), pygame.Color("#779556")]
  for row in range(DIMENSION):
    for col in range(DIMENSION):
      color = colors[(row + col) % 2 ]
      pygame.draw.rect(screen,color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        
"""
Draws the pieces on the board according to the current game estate
"""
def draw_pieces(screen, game_state):
  for row in range(DIMENSION):
    for col in range(DIMENSION):
      piece = game_state.board[row][col]
      if piece != 0:
        screen.blit(IMAGES[piece],pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
  
"""
Responsible for all graphics within a current game state
"""
def draw_states(screen, game_state):
  draw_board(screen)

  draw_pieces(screen,game_state)
  


"""
Selects piece or square on the board
"""
def mouse_click(game_state, move):
  if pygame.mouse.get_pressed()[0]:
        row, col = pygame.mouse.get_pos()
        row = math.ceil(row / 50) - 1
        col = math.ceil(col / 50) - 1

        return [row,col]
        
        # # Maybe put this part itself on its own function
        # selected_square = game_state.board[col][row]
        # if game_state.board[col][row] != 0 :
        #   move.piece = selected_square
        #   move.position = [col,row]
        #   move.selected = True
        # elif game_state.board[col][row] != 0 and move.selected:
        #   move.selected = False
        #   move.position.clear()
        #   move.piece = 0
        #   move.end_position.clear()

        # elif move.selected and not move.end_position:
        #     move.end_position = [col,row]
        #     game_state.board[move.position[0]][move.position[1]] = 0
        #     game_state.board[move.end_position[0]][move.position[1]] = move.piece

        #     # Reset move.piece , move.end_position, move.position
        #     move.selected = False
        
          
             
        
        return [row,col]

# def highlight_piece(screen, move):
#   color = pygame.Color("#baca49")
#   color2 = pygame.Color("pink")
#   if move.selected:
#     pygame.draw.rect(screen,color, pygame.Rect(move.position[1] * SQUARE_SIZE, move.position[0] * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
#   elif move.selected and len(move.position) != 0:
#     pygame.draw.rect(screen,color2, pygame.Rect(move.position[1] * SQUARE_SIZE, move.position[0] * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    

# Highlight selected piece 
# 
# 
# 
        
if __name__ == "__main__":
  main()

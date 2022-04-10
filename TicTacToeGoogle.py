import pygame, sys
import numpy as np
#so we can call numpy fcts as np.fct_name
pygame.init() #Need to initialize to use pygame
#Pygame - y vals increase downwards, x vals increase right
#Screen Settings/Constants
WIDTH = 600
HEIGHT = 600 #label constant vars in all caps
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLUMNS = 3
CIRCLERAD = 60
CIRCLEWID = 15
CROSSWIDTH = 25
SPACE = 45
BG_Color = (18,189,172) 
Line_Color = (12, 162, 146)
Gray = (84,84,84)
White = (243,235,211)

screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Tic-Tac-Toe")
screen.fill(BG_Color)

#Console Board ~ Numpy part
board = np.zeros((BOARD_ROWS,BOARD_COLUMNS))

#TicTacToe Lines
def draw_lines():
    pygame.draw.line(screen, Line_Color,(0,200), (600,200), LINE_WIDTH)
    pygame.draw.line(screen, Line_Color,(0,400), (600,400), LINE_WIDTH)
    pygame.draw.line(screen, Line_Color,(200,0), (200,600), LINE_WIDTH)
    pygame.draw.line(screen, Line_Color,(400,0), (400,600), LINE_WIDTH)
draw_lines()

# Tic Tac Toe Figures #for loop runs through board
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, White, (int(col * 200 + 200 / 2), int(row * 200 + 200 / 2)), CIRCLERAD, CIRCLEWID)
            elif board[row][col] == 2:
                pygame.draw.line(screen, Gray, (col*200 + SPACE,row*200 +200 - SPACE), (col * 200+200 - SPACE, row *200 +SPACE), CROSSWIDTH)
                pygame.draw.line(screen, Gray, (col*200 + SPACE,row*200 +SPACE), (col * 200+200 - SPACE, row *200 + 200 -SPACE), CROSSWIDTH)
#Square Fcts (From np.zeros fct)
def mark_square(row,col,player):
    board[row][col] = player #[]- index. 
def available_square(row,col):
    return board[row][col] == 0 #if/else shorter
def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS):
            if board[row][col] == 0:
                return False
    return True

#Game Functions
def check_win(player):
    for col in range(BOARD_COLUMNS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player: 
            draw_vert_win_line(col,player)
            return True #break fct and don't do others
    for row in range(BOARD_COLUMNS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player: 
            draw_horz_win_line(row,player)
            return True
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diag(player)
        return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diag(player)
        return True
    return False
def draw_vert_win_line(col, player):
    posX = col * 200 + 100
    if player == 1:
        color = White
    elif player == 2:
        color = Gray
    pygame.draw.line(screen, color, (posX,15), (posX, HEIGHT - 15), 15)
def draw_horz_win_line(row, player):
    posY = row * 200 + 100
    if player == 1:
        color = White
    elif player == 2:
        color = Gray
    pygame.draw.line(screen, color, (15,posY),(WIDTH - 15, posY), 15)
def draw_asc_diag(player):
    if player == 1:
        color = White
    elif player == 2:
        color = Gray
    pygame.draw.line(screen, color, (15, HEIGHT-15), (WIDTH -15, 15), 15)
def draw_desc_diag(player):
    if player == 1:
        color = White
    elif player == 2:
        color = Gray
    pygame.draw.line(screen, color, (15, 15 ), (WIDTH -15, HEIGHT-15), 15)
def restart():
    screen.fill(BG_Color)
    draw_lines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS): 
            board[row][col] = 0
#mainLoop (copy paste to start program)
player = 1
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over: #linking console to screen board
            mouseX = event.pos[0] #x coord
            mouseY = event.pos[1] #y coord
            clicked_row = int(mouseY // 200)#floor 
            clicked_col = int(mouseX // 200)
            if available_square(clicked_row, clicked_col ): 
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    if check_win(player):
                        game_over = True
                    player = 2
                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    if check_win(player):
                        game_over = True
                    player = 1
                draw_figures()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart() 
                game_over = False   
    pygame.display.update() #Need to update to show screen changes from settings


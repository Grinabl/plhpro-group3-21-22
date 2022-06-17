from tkinter import *
from tkinter import messagebox
from scrollable import *

def scorePage(name):
    global _scores
    global _scoresPage
    
    _scores = Toplevel()
    _scoresPage = Scores2Page(_scores,name)
    _scores.mainloop()

class Scores2Page:
    def __init__(self,top=None, name="") :
        self.name_label = Label(top)
        self.name_label.place(x=0,y=0)
        self.name_label.configure(text=name)

def create_players_rect(name1, name2, score1, score2, start_row, start_column, top_1, round_num, match_num):
    game_title_label = Label(top_1, text=f"ΓΥΡΟΣ: {str(round_num)} ΠΑΙΧΝΙΔΙ: {str(match_num)}")
    game_title_label.grid(row=start_row, column=start_column)
    player1_name_label = Label(top_1, text=name1)
    player1_name_label.grid(row=start_row+1, column=start_column, padx=(20,10))
    player2_name_label = Label(top_1, text=name2)
    player2_name_label.grid(row=start_row+2, column=start_column)
    player1_score_label = Label(top_1, text=str(score1))
    player1_score_label.grid(row=start_row+1, column=start_column+1)
    player2_score_label = Label(top_1, text=str(score2))
    player2_score_label.grid(row=start_row+2, column=start_column+1)
    score_btn = Button(top_1, text="SCORE")
    # player1_name_label = Label(top_1, text=name1)
    # player1_name_label.grid(row=start_row, column=start_column, padx=(20,10))
    # player2_name_label = Label(top_1, text=name2)
    # player2_name_label.grid(row=start_row+1, column=start_column)
    # player1_score_label = Label(top_1, text=str(score1))
    # player1_score_label.grid(row=start_row, column=start_column+1)
    # player2_score_label = Label(top_1, text=str(score2))
    # player2_score_label.grid(row=start_row+1, column=start_column+1)
    # score_btn = Button(top_1, text="SCORE")
    
    score_btn.configure(command=lambda name1=name1: showMessage(name1))
    score_btn.grid(row=start_row, column=start_column+2)

def showMessage(name):
    scorePage(name)


root = Tk()
root.geometry("1300x700")
frame = ScrollableFrame(root)
'''set dimensions of the frame'''
frame.configure(width=1300, height=700)
# frame.pack(fill="both", expand=True)

_size = 6
_columns = _size + 1
WIDTH = int(1300)
HEIGHT = 700
_column_width = WIDTH / _columns
#_game_box_width = _column_width - HORIZONTAL_PADDING
#_game_box_height = _game_box_width / GAME_BOX_WIDTH_HEIGHT_RATIO
row = 0
column = 0
for i in range(_columns):
    matches = 2 ** abs(i - _size)
    for j in range(matches):
        create_players_rect(f"first-r{str(i + 1)}-g{str(j + 1)}-x{str(row)}-y{str(column)}", f"second-r{str(i + 1)}-g{str(j + 1)}", 0, 0, row, column, frame.scrollable_frame, i + 1, j + 1)
        if (i == 0):
            row += 8     
        elif (i == 1):
            row += 16
        elif (i == 2):
            row += 32
        elif (i == 3):
            row += 64
        elif (i == 4):
            row += 128
        elif (i == 5):
            row += 256
        elif (i == 6):
            row += 512
    if (i == 0):
        row = 4
    elif (i == 1):
        row = 12
    elif (i == 2):
        row = 28
    elif (i == 3):
        row = 60
    elif (i == 4):
        row = 124
    elif (i == 5):
        row = 252
    elif (i == 6):
        row = 508
    column += 4  

frame.pack(fill="both", expand=True)

root.mainloop()

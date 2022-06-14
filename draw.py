
import sqlite3
import random


class Draw():
    
    def create_db_connection(db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        return conn

    def clear_matches(conn, cur):
        cur.execute("""DROP TABLE IF EXISTS Matches""")
        conn.commit()
    
    def insert_db_header(conn, cur):
        cur.execute("""CREATE TABLE IF NOT EXISTS Matches (Id text NOT NULL, Player1Id integer NOT NULL, Player2Id integer NOT NULL, Player1Score integer NOT NULL, Player2Score integer NOT NULL);""")
        conn.commit()
    
    def run_draw():
        conn = Draw.create_db_connection('database.db')
        cur = conn.cursor()
        Draw.clear_matches(conn, cur)
        Draw.insert_db_header(conn, cur)
        conn.row_factory = lambda cursor, row: row[0]
        playersList = cur.execute("SELECT actual_rank FROM players order by actual_rank asc").fetchall() # get players ids from database table players
        rankGroups = [playersList[x:x+16] for x in range(0, len(playersList), 16)]
        groups = {}
 
 
        for i in range(1, 17):
            groups[i] = []
            for j in range(1, 9):
                random.shuffle(rankGroups[j-1])
                player = rankGroups[j-1].pop()
                groups[i].append(player)
        # print(groups)
        
        # matches = {}
        for i in range(1, 17):
            for j in range(1, 5):
                matchId = '1.' + str(i) + '.' + str(j)
                random.shuffle(groups[i])
                cur.execute("""INSERT INTO Matches (Id,Player1Id,Player2Id,Player1Score,Player2Score) VALUES (?,?,?,?,?);""", (matchId, groups[i].pop(), groups[i].pop(), 0, 0))
                conn.commit()
        
        


# # with sqlite3.connect('database.db') as db:
# #         db.row_factory = lambda cursor, row: row[0]
# #         cur = db.cursor()
# #         cur.execute("""CREATE TABLE IF NOT EXISTS Matches (Id text NOT NULL, Player1Id integer NOT NULL, Player2Id integer NOT NULL, Player1Score integer NOT NULL, Player2Score integer NOT NULL);""")
# #         db.commit()
# #         db.close()



# def initialize_db(conn)


# playersInDb = cur.execute("SELECT actual_rank FROM players order by actual_rank asc").fetchall() # get players ids from database table players

# groupsByRank = [playersInDb[x:x+16] for x in range(0, len(playersInDb), 16)] # create 8 groups of players by rank

# # Initial groups of players from each group
# initialGroups = {} 
  
# for i in range(1, 17):
#     initialGroups[i] = []
#     for j in range(1, 9):
#        random.shuffle(groupsByRank[j-1])
#        player = groupsByRank[j-1].pop()
#        initialGroups[i].append(player)

# for i in range(1, 17):
#     for j in range(1, 5):
#         matchId = '1.' + str(i) + '.' + str(j)
#         random.shuffle(initialGroups[i])
#         cur.execute("""INSERT INTO Matches (Id,Player1Id,Player2Id,Player1Score,Player2Score) VALUES (?,?,?,?,?);""", (matchId, initialGroups[i].pop(), initialGroups[i].pop(), 0, 0))
#         db.commit()

# import math
# import random
# import tkinter
# from tkinter import *
# from Pairing import *

# ranks_of_all_groups = (FillListOfPairRanks())
# final_pairing = CreatePairsInsideGroups(ranks_of_all_groups)
# print(final_pairing)
# print()

# root = Tk()

# def insert_val(e1, e2):
#     print(e1.get(), e2.get())    

# def popup_window(event):
#     top = Toplevel(root)
    
#     top.geometry("300x180")
#     top.title("Insert Score")
    
#     l1 = Label(top, text = "Player 1").place(x = 30, y = 50)
#     l2 = Label(top, text = "Player 2").place(x = 100, y = 50)

#     e1 = Entry(top)
#     e1.place(x = 10, y = 70)
#     e2 = Entry(top)
#     e2.place(x = 100, y = 70)

#     button = Button(top, text = "Place Score", command = lambda:insert_val(e1, e2)).pack(pady = 10, side = TOP)

#     winner = max(e1.get(), e2.get())
#     print(winner)
    
#     top.mainloop()
    
# class ScrollBar:
#     def __init__(self):
        

#         h = Scrollbar(root, orient='horizontal')
#         h.pack(side=BOTTOM, fill=X)
        
#         v = Scrollbar(root)
#         v.pack(side=RIGHT, fill=Y)

#         HEIGHT = 2048  
#         WIDTH = 1200
#         HORIZONTAL_PADDING = 60
#         GAME_BOX_WIDTH_HEIGHT_RATIO = 3

#         _size = 6
#         _columns = _size + 1

#         _column_width = WIDTH / _columns

#         _game_box_width = _column_width - HORIZONTAL_PADDING
#         _game_box_height = _game_box_width / GAME_BOX_WIDTH_HEIGHT_RATIO

#         canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT)
#         canvas.pack()

#         for i in range(_columns):
#             games = 2 ** abs(i - _size)
            
#             x_center = _column_width * (i + 0.5)
#             y_size = HEIGHT / games
#             for j in range(games):
#                 name1 = final_pairing[0][(j)%8][0]
#                 name2 = final_pairing[0][(j)%8][1]
#                 y_center = y_size * (j + 0.5)
#                 canvas.create_rectangle(x_center - _game_box_width / 2, y_center - _game_box_height / 2,
#                                         x_center + _game_box_width / 2, y_center + _game_box_height / 2)
                

#                 canvas.create_text(x_center - _game_box_width / 2 + 50, y_center - _game_box_height / 2 + 12, text=name1, fill="black")
#                 canvas.create_text(x_center - _game_box_width / 2 + 50, y_center - _game_box_height / 2 + 25, text=name2, fill="black")
                
#                 if i != _columns - 1:
#                     canvas.create_line(x_center + _game_box_width / 2, y_center,
#                                        x_center + _game_box_width / 2 + HORIZONTAL_PADDING / 2, y_center)
#                 if i != 0:
#                     canvas.create_line(x_center - _game_box_width / 2, y_center, x_center - _game_box_width / 2 - HORIZONTAL_PADDING / 2, y_center)
#                 if j % 2 == 1:
#                     canvas.create_line(x_center + _game_box_width / 2 + HORIZONTAL_PADDING / 2, y_center, x_center + _game_box_width / 2 + HORIZONTAL_PADDING / 2, y_center - y_size)

#                 btn = canvas.create_rectangle(x_center +  _game_box_width / 10  + 30, y_center - _game_box_height / 10, x_center + _game_box_width / 10 + 10, y_center + _game_box_height / 10, fill = "red")
#                 canvas.tag_bind(btn, "<Button-1>", popup_window)
               
#                 #final_pairing = GetUserInput()       
#         canvas.pack()
#         h.config(command=canvas.xview)
#         v.config(command=canvas.yview)
#         root.mainloop()
# s = ScrollBar()



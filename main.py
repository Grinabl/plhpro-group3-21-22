from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox

from draw import Draw


root = Tk()
root.geometry("1366x768")
bg = PhotoImage(file = "images/Australian_Open_logo.png")
root.title("ΠΛΗΠΡΟ - ΟΜΑΔΑ03")
root.resizable(0, 0)

with sqlite3.connect('database.db') as db:
        cur = db.cursor()



def players_list():
    root.withdraw()
    global players
    global playersPage
    players = Toplevel()
    playersPage = PlayerList(players)
    players.mainloop()

def games_page():
    root.withdraw()
    global games
    global gamesPage
    games=Toplevel()
    gamesPage=GamesPage(games)
    games.mainloop()

class MainPage: # Αρχική Σελίδα
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("AUSTRALIAN OPEN - ΠΛΗΠΡΟ - ΟΜΑΔΑ03")

        self.logo_label = Label(root)
        self.logo_label.place(relx=0.85, rely=0.92, width=205, height=60)
        self.logo_label.configure(image=bg)
        # self.logo2_label = Label(root)
        # self.logo2_label.place(relx=0.85, rely=0.92, width=205, height=60)
        # self.logo2_label.configure(text="TESTTSTS")
        # self.logo2_label.configure(background='transparent')

        self.playersMenuBtn = Button(root)
        self.playersMenuBtn.place(relx=0.14, rely=0.1, width=250, height=80)
        self.playersMenuBtn.configure(relief="flat")
        self.playersMenuBtn.configure(overrelief="flat")
        self.playersMenuBtn.configure(activebackground="#CF1E14")
        self.playersMenuBtn.configure(cursor="hand2")
        self.playersMenuBtn.configure(foreground="#ffffff")
        self.playersMenuBtn.configure(background="#CF1E14")
        self.playersMenuBtn.configure(font="-family {Poppins SemiBold} -size 24")
        self.playersMenuBtn.configure(borderwidth="0")
        self.playersMenuBtn.configure(text="""ΠΑΙΚΤΕΣ""")
        self.playersMenuBtn.configure(command=players_list)

        self.gamesMenuBtn = Button(root)
        self.gamesMenuBtn.place(relx=0.54, rely=0.1, width=250, height=80)
        self.gamesMenuBtn.configure(relief="flat")
        self.gamesMenuBtn.configure(overrelief="flat")
        self.gamesMenuBtn.configure(activebackground="#CF1E14")
        self.gamesMenuBtn.configure(cursor="hand2")
        self.gamesMenuBtn.configure(foreground="#ffffff")
        self.gamesMenuBtn.configure(background="#CF1E14")
        self.gamesMenuBtn.configure(font="-family {Poppins SemiBold} -size 24")
        self.gamesMenuBtn.configure(borderwidth="0")
        self.gamesMenuBtn.configure(text="""ΑΓΩΝΕΣ""")
        self.gamesMenuBtn.configure(command=games_page)
        

class PlayerList: # Σελίδα λίστας παικτών
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("AUSTRALIAN OPEN - ΠΛΗΠΡΟ - ΟΜΑΔΑ03 - ΛΙΣΤΑ ΠΑΙΚΤΩΝ")

        self.sel_player_name_label = Label(players)
        self.sel_player_name_label.place(relx=0.800, rely=0.05)
        self.sel_player_name_label.configure(font="-family {Poppins SemiBold} -size 20")
        

        self.sel_player_surname_label = Label(players)
        self.sel_player_surname_label.place(relx=0.800, rely=0.10)
        self.sel_player_surname_label.configure(font="-family {Poppins SemiBold} -size 20")
        

        self.sel_player_birth_date_label = Label(players)
        self.sel_player_birth_date_label.place(relx=0.800, rely=0.15)
        self.sel_player_birth_date_label.configure(font="-family {Poppins SemiBold} -size 10")
        
        
        self.sel_player_birth_place_label = Label(players)
        self.sel_player_birth_place_label.place(relx=0.800, rely=0.20)
        self.sel_player_birth_place_label.configure(font="-family {Poppins SemiBold} -size 10")
        

        self.sel_player_rank = Label(players)
        self.sel_player_rank.place(relx=0.700, rely=0.05)
        self.sel_player_rank.configure(font="-family {Poppins SemiBold} -size 30")
        


        #region Label Αναζήτησης
        self.player_search_label = Label(players)
        self.player_search_label.place(relx=0, rely=0.005, width=100, height=28)
        self.player_search_label.configure(text="ΕΠΙΘΕΤΟ: ")
        self.player_search_label.configure(font="-family {Poppins SemiBold} -size 10")
        #endregion
        #region Πεδίο αναζήτησης
        self.search_player_entry = Entry(players)
        self.search_player_entry.place(relx=0.065, rely=0.005, width=210, height=28)
        self.search_player_entry.configure(font="-family {Poppins} -size 10")
        self.search_player_entry.configure(relief="flat")
        #endregion
        #region Button αναζήτησης
        self.search_player_button = Button(players)
        self.search_player_button.place(relx=0.229, rely=0.005, width=100, height=28)
        self.search_player_button.configure(relief="flat")
        self.search_player_button.configure(overrelief="flat")
        self.search_player_button.configure(activebackground="#CF1E14")
        self.search_player_button.configure(cursor="hand2")
        self.search_player_button.configure(foreground="#ffffff")
        self.search_player_button.configure(background="#CF1E14")
        self.search_player_button.configure(font="-family {Poppins SemiBold} -size 10")
        self.search_player_button.configure(borderwidth="0")
        self.search_player_button.configure(text="""ΑΝΑΖΗΤΗΣΗ""")
        self.search_player_button.configure(command=self.search_players_list)
        #endregion
        
        #region Tree λίστα παικτών
        self.tree = ttk.Treeview(players)
        self.tree.place(relx=0.005, rely=0.05, width=700, height=660)
        self.tree.configure(selectmode="extended")
        self.tree.configure(
            columns=(
                "actual_rank",
                "firstname",
                "lastname",
                "yearofbirth",
                "birthplace",
                "sqlrank",
            )
        )
        self.tree.heading("actual_rank", text="ID", anchor=W)
        self.tree.heading("firstname", text="ONOMA", anchor=W)
        self.tree.heading("lastname", text="ΕΠΙΘΕΤΟ", anchor=W)
        self.tree.heading("yearofbirth", text="ΕΤΟΣ ΓΕΝ.", anchor=W)
        self.tree.heading("birthplace", text="ΠΟΛΗ", anchor=W)
        self.tree.heading("sqlrank", text="RANK", anchor=W)
        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=40)
        self.tree.column("#2", stretch=NO, minwidth=0, width=120)
        self.tree.column("#3", stretch=NO, minwidth=0, width=120)
        self.tree.column("#4", stretch=NO, minwidth=0, width=60)
        self.tree.column("#5", stretch=NO, minwidth=0, width=200)
        self.tree.column("#6", stretch=NO, minwidth=0, width=50)

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        #vertical scrollbar για το πεδίο παικτών
        self.vsb = ttk.Scrollbar(players, orient="vertical", command=self.tree.yview)
        self.vsb.place(relx=0.506, rely=0.05, relheight=0.86)
        self.tree.configure(yscrollcommand=self.vsb.set)
        #endregion
        # επιστροφη στο μενου
        self.exit_button = Button(players)
        self.exit_button.place(relx=0.835, rely=0.005, width=200, height=23)
        self.exit_button.configure(relief="flat")
        self.exit_button.configure(overrelief="flat")
        self.exit_button.configure(activebackground="#CF1E14")
        self.exit_button.configure(cursor="hand2")
        self.exit_button.configure(foreground="#ffffff")
        self.exit_button.configure(background="#CF1E14")
        self.exit_button.configure(font="-family {Poppins SemiBold} -size 10")
        self.exit_button.configure(borderwidth="0")
        self.exit_button.configure(text="""ΕΠΙΣΤΡΟΦΗ ΣΤΟ MENU""")
        self.exit_button.configure(command=self.Exit)

        self.fetch_data() # Αρχικοποίηση δεδομένων

    def fetch_data(self):
        cur.execute("SELECT actual_rank, firstname,lastname,yearofbirth,birthplace,sglrank FROM players order by actual_rank asc")
        fetch = cur.fetchall()
        for data in fetch:
            self.tree.insert("", "end", values=(data))

    def search_players_list(self):
        self.tree.delete(*self.tree.get_children())
        player_lastname = self.search_player_entry.get()
        cur.execute("SELECT actual_rank, firstname,lastname,yearofbirth,birthplace,sglrank FROM players where lastname like '%" + player_lastname + "%' order by actual_rank asc")
        fetch = cur.fetchall()
        for data in fetch:
            self.tree.insert("", "end", values=(data))

    def on_tree_select(self, Event):
        player_actual_rank = self.tree.item(self.tree.selection()[0])["values"][0]
        cur.execute("SELECT actual_rank, firstname,lastname,yearofbirth,birthplace,sglrank FROM players where actual_rank=" + str(player_actual_rank))
        player_result = cur.fetchone()
        if len(player_result)==0:
            messagebox.showerror(message='Player not found')
        else:
            self.sel_player_name_label.configure(text=player_result[1])
            self.sel_player_surname_label.configure(text=player_result[2])
            self.sel_player_birth_date_label.configure(text=str(player_result[3]))
            self.sel_player_birth_place_label.configure(text=player_result[4])
            self.sel_player_rank.configure(text=str(player_result[5]))
        
    
    def show_selected_player_data(self, actual_rank):
        pass

    def Exit(self):
        players.destroy()
        root.deiconify()

class GamesPage: # Σελίδα Αγώνων
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("AUSTRALIAN OPEN - ΠΛΗΠΡΟ - ΟΜΑΔΑ03 - ΑΓΩΝΕΣ")

        
        
        # self.tree.configure(yscrollcommand=self.vsb.set)
        

        # επιστροφη στο μενου
        self.exit_button = Button(games)
        self.exit_button.place(relx=0.835, rely=0.005, width=200, height=23)
        self.exit_button.configure(relief="flat")
        self.exit_button.configure(overrelief="flat")
        self.exit_button.configure(activebackground="#CF1E14")
        self.exit_button.configure(cursor="hand2")
        self.exit_button.configure(foreground="#ffffff")
        self.exit_button.configure(background="#CF1E14")
        self.exit_button.configure(font="-family {Poppins SemiBold} -size 10")
        self.exit_button.configure(borderwidth="0")
        self.exit_button.configure(text="""ΕΠΙΣΤΡΟΦΗ ΣΤΟ MENU""")
        self.exit_button.configure(command=self.Exit)

        # Draw button
        self.draw_button = Button(games)
        self.draw_button.place(relx=0.035, rely=0.005, width=200, height=23)
        self.draw_button.configure(relief="flat")
        self.draw_button.configure(overrelief="flat")
        self.draw_button.configure(activebackground="#CF1E14")
        self.draw_button.configure(cursor="hand2")
        self.draw_button.configure(foreground="#ffffff")
        self.draw_button.configure(background="#CF1E14")
        self.draw_button.configure(font="-family {Poppins SemiBold} -size 10")
        self.draw_button.configure(borderwidth="0")
        self.draw_button.configure(text="""ΚΛΗΡΩΣΗ""")
        self.draw_button.configure(command=self.create_draw)



        ########
        # h = Scrollbar(games, orient='horizontal')
        # h.pack(side=BOTTOM, fill=X)
        
        # v = Scrollbar(games)
        # v.pack(side=RIGHT, fill=Y)

        HEIGHT = 2048  
        WIDTH = 1366
        HORIZONTAL_PADDING = 60
        GAME_BOX_WIDTH_HEIGHT_RATIO = 4

        _size = 6
        _columns = _size + 1

        _column_width = WIDTH / _columns

        _game_box_width = _column_width - HORIZONTAL_PADDING
        _game_box_height = _game_box_width / GAME_BOX_WIDTH_HEIGHT_RATIO

        self.canvas = Canvas(games, width=WIDTH, height=HEIGHT)
        self.canvas.place(relx=0.05, rely=0.15, relheight=0.90)
        self.canvas.pack()

        for i in range(_columns):
            matches = 2 ** abs(i - _size)
            
            x_center = _column_width * (i + 0.5)
            y_size = HEIGHT / matches
            for j in range(matches):
                # name1 = final_pairing[0][(j)%8][0]
                # name2 = final_pairing[0][(j)%8][1]
                y_center = y_size * (j + 0.5)
                self.canvas.create_rectangle(x_center - _game_box_width / 2, y_center - _game_box_height / 2,
                                        x_center + _game_box_width / 2, y_center + _game_box_height / 2)
                

                self.canvas.create_text(x_center - _game_box_width / 2 + 50, y_center - _game_box_height / 2 + 12, text="name1", fill="black")
                self.canvas.create_text(x_center - _game_box_width / 2 + 50, y_center - _game_box_height / 2 + 25, text="name2", fill="black")
                
                if i != _columns - 1:
                    self.canvas.create_line(x_center + _game_box_width / 2, y_center,
                                       x_center + _game_box_width / 2 + HORIZONTAL_PADDING / 2, y_center)
                if i != 0:
                    self.canvas.create_line(x_center - _game_box_width / 2, y_center, x_center - _game_box_width / 2 - HORIZONTAL_PADDING / 2, y_center)
                if j % 2 == 1:
                    self.canvas.create_line(x_center + _game_box_width / 2 + HORIZONTAL_PADDING / 2, y_center, x_center + _game_box_width / 2 + HORIZONTAL_PADDING / 2, y_center - y_size)

                # btn = canvas.create_rectangle(x_center +  _game_box_width / 10  + 30, y_center - _game_box_height / 10, x_center + _game_box_width / 10 + 10, y_center + _game_box_height / 10, fill = "red")
                # canvas.tag_bind(btn, "<Button-1>", popup_window)
               
                #final_pairing = GetUserInput()       
        self.canvas.pack()
        # h.config(command=canvas.xview)
        # v.config(command=canvas.yview)
        # self.vsb = ttk.Scrollbar(games, orient="vertical", command=self.tree.yview)
        self.vsb = ttk.Scrollbar(games, orient="vertical")
        self.vsb.place(relx=0.95, rely=0.15, relheight=0.86)
        # self.hsb = ttk.Scrollbar(games, orient="horizontal", command=self.tree.xview)
        self.hsb = ttk.Scrollbar(games, orient="horizontal")
        self.vsb.config(command=self.canvas.yview)
        self.hsb.config(command=self.canvas.xview)
        ########
        
    def create_draw():
        draw = Draw()
        draw.run_draw()

        

    def Exit(self):
        games.destroy()
        root.deiconify()

mainPage = MainPage(root)
root.mainloop()
from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
import webbrowser
from scrollable import *
from data_parser import parsing_gui
from draw import run_draw

#Κλήση του Tkinter και αρχικοποίηση της οθόνης
root = Tk()
root.geometry("1366x768")
bg = PhotoImage(file = "images/Australian_Open_logo.png")
root.title("ΠΛΗΠΡΟ - ΟΜΑΔΑ03")
root.resizable(0, 0)
with sqlite3.connect('database.db') as db:
        cur = db.cursor()
        
#Συνάρτηση που εμφανίζει τη σελίδα με τους παιχτές της ομάδας
def players_list():
    root.withdraw()
    global players
    global playersPage
    players = Toplevel()
    playersPage = PlayerList(players)
    players.mainloop()

#Συνάρτηση που εμφανίζει τη σελίδα με τους αγώνες
def games_nocanvas_page():
    root.withdraw()
    global gamesNoCanvas
    global gaesNoCanvasPage
    gamesNoCanvas = Toplevel()
    gaesNoCanvasPage = GamesNoCanvasPage(gamesNoCanvas)
    gamesNoCanvas.mainloop()
    
#Συνάρτηση που εμφανίζει τη σελίδα σχετικά με τους Συντελεστές   
def about_page():
    root.withdraw()
    global about
    global aboutPage
    about=Toplevel()
    aboutPage=AboutPage(about)
    about.mainloop()

#Συνάρτηση που εμφανίζει τη σελίδα καταχώρησης του σκορ
def score_page(match_id,next_round_id,name1,name2):
    gamesNoCanvas.withdraw()
    global scoresPopup
    global scoresPage
    scoresPopup = Toplevel()
    scoresPage = ScoresPage(scoresPopup,match_id,next_round_id,name1,name2)
    scoresPopup.mainloop()

class MainPage: # Αρχική Σελίδα
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("AUSTRALIAN OPEN - ΠΛΗΠΡΟ - ΟΜΑΔΑ03")
        #Label εικόνας
        self.logo_label = Label(root)
        self.logo_label.place(relx=0.85, rely=0.92, width=205, height=60)
        self.logo_label.configure(image=bg)
        #End region Label εικόνας

        #Πλήκτρο ανακατεύθυνσης στη σελίδα με τους παίκτες
        self.playersMenuBtn = Button(root)
        self.playersMenuBtn.place(relx=0.10, rely=0.1, width=250, height=80)
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
        #End region πλήκτρου ανακατεύθυνσης

        #Πλήκτρο ανακατεύθυνσης στη σελίδα με τις αγώνες
        self.gamesMenuBtn = Button(root)
        self.gamesMenuBtn.place(relx=0.70, rely=0.1, width=250, height=80)
        self.gamesMenuBtn.configure(relief="flat")
        self.gamesMenuBtn.configure(overrelief="flat")
        self.gamesMenuBtn.configure(activebackground="#CF1E14")
        self.gamesMenuBtn.configure(cursor="hand2")
        self.gamesMenuBtn.configure(foreground="#ffffff")
        self.gamesMenuBtn.configure(background="#CF1E14")
        self.gamesMenuBtn.configure(font="-family {Poppins SemiBold} -size 24")
        self.gamesMenuBtn.configure(borderwidth="0")
        self.gamesMenuBtn.configure(text="""ΑΓΩΝΕΣ""")
        self.gamesMenuBtn.configure(command=games_nocanvas_page)
        #End region πλήκτρου ανακατεύθυνσης

        #Πλήκτρο ανακατεύθυνσης στη σελίδα αρχικοποίησης της βάσης
        self.init_db = Button(root)
        self.init_db.place(relx=0.40, rely=0.4, width=250, height=100)
        self.init_db.configure(relief="flat")
        self.init_db.configure(overrelief="flat")
        self.init_db.configure(activebackground="#CF1E14")
        self.init_db.configure(cursor="hand2")
        self.init_db.configure(foreground="#ffffff")
        self.init_db.configure(background="#CF1E14")   
        self.init_db.configure(font="-family {Poppins SemiBold} -size 24")
        self.init_db.configure(borderwidth="0")
        self.init_db.configure(text="""ΑΡΧΙΚΟΠΟΙΗΣΗ""")
        self.init_db.configure(command=parsing_gui)
        #End region πλήκτρου ανακατεύθυνσης

        #Πλήκτρο ανακατεύθυνσης στη σελίδα του Github
        self.github_pg = Button(root)
        self.github_pg.place(relx=0.10, rely=0.4, width=250, height=100)
        self.github_pg.configure(relief="flat")
        self.github_pg.configure(overrelief="flat")
        self.github_pg.configure(activebackground="#CF1E14")
        self.github_pg.configure(cursor="hand2")
        self.github_pg.configure(foreground="#ffffff")
        self.github_pg.configure(background="#CF1E14")
        self.github_pg.configure(font="-family {Poppins SemiBold} -size 24")
        self.github_pg.configure(borderwidth="0")
        self.github_pg.configure(text="""Github""")
        self.github_pg.configure(command=lambda: webbrowser.open("https://github.com/Grinabl/plhpro-group3-21-22"))
        #End region πλήκτρου ανακατεύθυνσης

        #Πλήκτρο ανακατεύθυνσης στη σελίδα των συντελεστών
        self.abt_pg = Button(root)
        self.abt_pg.place(relx=0.70, rely=0.4, width=250, height=100)
        self.abt_pg.configure(relief="flat")
        self.abt_pg.configure(overrelief="flat")
        self.abt_pg.configure(activebackground="#CF1E14")
        self.abt_pg.configure(cursor="hand2")
        self.abt_pg.configure(foreground="#ffffff")
        self.abt_pg.configure(background="#CF1E14")
        self.abt_pg.configure(font="-family {Poppins SemiBold} -size 24")
        self.abt_pg.configure(borderwidth="0")
        self.abt_pg.configure(text="""ΣΥΝΤΕΛΕΣΤΕΣ""")
        self.abt_pg.configure(command=about_page)
        #End region πλήκτρου ανακατεύθυνσης
                
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

        #player games frame
        self.player_games_frame = Frame(players)
        self.player_games_frame.place(relx=0.6, rely=0.4,width=400)

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
        if len(self.tree.selection()) > 0:
            player_actual_rank = self.tree.item(self.tree.selection()[0])["values"][0]
            self.show_selected_player_profile_data(player_actual_rank)
            self.show_selected_player_games_data(player_actual_rank)


    def show_selected_player_profile_data(self, actual_rank):
        player_data = cur.execute("SELECT actual_rank, firstname,lastname,yearofbirth,birthplace,sglrank FROM players where actual_rank=?", (actual_rank,)).fetchall()
        if len(player_data[0]) > 0:
            self.sel_player_name_label.configure(text=player_data[0][1])
            self.sel_player_surname_label.configure(text=player_data[0][2])
            self.sel_player_birth_date_label.configure(text=str(player_data[0][3]))
            self.sel_player_birth_place_label.configure(text=player_data[0][4])
            self.sel_player_rank.configure(text=str(player_data[0][5]))

    def show_selected_player_games_data(self, actual_rank):
        player_games = []
        player_games = cur.execute("SELECT Id,Player1Id, Player2Id, Player1Score, Player2Score FROM Matches WHERE Player1Id=? OR Player2Id=?", (actual_rank, actual_rank,)).fetchall()
        self.populate_player_games(player_games)
        
    def populate_player_games(self,player_games):
        self.player_games_frame.destroy()
        self.player_games_frame = Frame(players)
        self.player_games_frame.place(relx=0.6, rely=0.3, width=500, height=500)
        if len(player_games) > 0:
            r_x=0.0
            r_y=0.0
            for game in sorted(player_games, key=lambda data: data[0]):
                player1_data = cur.execute("SELECT actual_rank, firstname,lastname,yearofbirth,birthplace,sglrank FROM players where actual_rank=?", (game[1],)).fetchall()
                player2_data = cur.execute("SELECT actual_rank, firstname,lastname,yearofbirth,birthplace,sglrank FROM players where actual_rank=?", (game[2],)).fetchall()
                if len(player1_data) > 0:
                    group_label = Label(self.player_games_frame)
                    group_label.place(relx=r_x, rely=r_y)
                    group_label.configure(font="-family {Poppins SemiBold} -size 12", anchor=W)
                    if len(game[0]) > 3:
                        group_label.configure(text=f'ΓΥΡΟΣ: {game[0][0]} GROUP: {game[0][2]} MATCH: {game[0][4]}')
                    else:
                        group_label.configure(text=f'ΓΥΡΟΣ: {game[0][0]} MATCH: {game[0][2]}')
                    r_y += 0.06
                    game_title_label = Label(self.player_games_frame)
                    game_title_label.place(relx=r_x, rely=r_y)
                    game_title_label.configure(text=player1_data[0][1] + " " + player1_data[0][2] + " vs " + player2_data[0][1] + " " + player2_data[0][2] + ": " + str(game[3]) + "-" + str(game[4]))
                    game_title_label.configure(font="-family {Poppins SemiBold} -size 12", anchor=W)
                    r_y += 0.08

    def Exit(self):
        players.destroy()
        root.deiconify()

class GamesNoCanvasPage:
    def __init__(self, top=None):
        top.geometry("1900x760")
        top.resizable(0, 0)
        top.title("AUSTRALIAN OPEN - ΠΛΗΠΡΟ - ΟΜΑΔΑ03 - ΑΓΩΝΕΣ")

        self.frame = ScrollableFrame(gamesNoCanvas)
        self.frame.configure(width=1300, height=700)

        # επιστροφη στο μενου
        self.exit_button = Button(gamesNoCanvas)
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

        # Κουμπί αρχικοποίησης κλήρωσης
        self.draw_button = Button(gamesNoCanvas)
        self.draw_button.place(relx=0.35, rely=0.005, width=200, height=23)
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

        _size = 6
        _columns = _size + 1
        row = 0
        column = 0
        prev_row = 4
        multiplier = 8
        add_param = 8
        for i in range(_columns):
            matches = 2 ** abs(i - _size)
            for j in range(matches):
                if (matches == 64):
                    external = j // 4 + 1
                    internal_num = j % 4 + 1
                    p_internal_num = 1 if (internal_num == 1 or internal_num == 2) else 2
                    match_id = str(i + 1) + '.' + str(external) + '.'  + str(internal_num)
                    next_round_id = str(i + 2) + '.' + str(external) + '.' + str(p_internal_num)
                    cur.execute("SELECT Id, Player1Id, Player2Id, Player1Score, Player2Score FROM Matches WHERE Id=?", (match_id,))
                    match_record = cur.fetchall()
                    if len(match_record) > 0:
                        player1_data = cur.execute("SELECT firstname, lastname from players where actual_rank = ?", (match_record[0][1],)).fetchall()
                        player2_data = cur.execute("SELECT firstname, lastname from players where actual_rank = ?", (match_record[0][2],)).fetchall()
                        name1 = player1_data[0][0] + ' ' + player1_data[0][1]
                        name2 = player2_data[0][0] + ' ' + player2_data[0][1]
                        score1=match_record[0][3]
                        score2=match_record[0][4]
                    else:
                        name1="N/A"
                        name2="N/A"
                        score1="N/A"
                        score2="N/A"
                elif (matches == 32):
                    external = j // 2 + 1
                    internal_num = j % 2 + 1
                    match_id = str(i + 1) + '.' + str(external) + '.' + str(internal_num)
                    next_round_id = str(i + 2) + '.' + str(external) + '.1'
                    cur.execute("SELECT Id, Player1Id, Player2Id, Player1Score, Player2Score FROM Matches WHERE Id=?", (match_id,))
                    match_record = cur.fetchall()
                    if len(match_record) > 0:
                        player1_data = cur.execute("SELECT firstname, lastname from players where actual_rank = ?", (match_record[0][1],)).fetchall()
                        player2_data = cur.execute("SELECT firstname, lastname from players where actual_rank = ?", (match_record[0][2],)).fetchall()
                        name1 = player1_data[0][0] + ' ' + player1_data[0][1]
                        name2 = "N/A" if (len(player2_data) < 1) else (player2_data[0][0] + ' ' + player2_data[0][1])
                        score1=match_record[0][3]
                        score2=match_record[0][4]
                    else:
                        name1="N/A"
                        name2="N/A"
                        score1="N/A"
                        score2="N/A"
                elif (matches == 16):
                    external = j + 1
                    internal_num = 1
                    p_external = (external + 1) // 2 if external % 2 == 1 else external // 2
                    match_id = str(i + 1) + '.' + str(external) + '.' + str(internal_num)
                    next_round_id = str(i + 2) + '.' + str(p_external)
                    cur.execute("SELECT Id, Player1Id, Player2Id, Player1Score, Player2Score FROM Matches WHERE Id=?", (match_id,))
                    match_record = cur.fetchall()
                    if len(match_record) > 0:
                        player1_data = cur.execute("SELECT firstname, lastname from players where actual_rank = ?", (match_record[0][1],)).fetchall()
                        player2_data = cur.execute("SELECT firstname, lastname from players where actual_rank = ?", (match_record[0][2],)).fetchall()
                        name1 = player1_data[0][0] + ' ' + player1_data[0][1]
                        name2 = "N/A" if (len(player2_data) < 1) else (player2_data[0][0] + ' ' + player2_data[0][1])
                        score1=match_record[0][3]
                        score2=match_record[0][4]
                    else:
                        name1="N/A"
                        name2="N/A"
                        score1="N/A"
                        score2="N/A"
                elif (matches == 8):
                    external = j + 1
                    p_external = (external + 1) // 2 if external % 2 == 1 else external // 2
                    match_id = str(i + 1) + '.' + str(external)
                    next_round_id = str(i + 2) + '.' + str(p_external)
                    cur.execute("SELECT Id, Player1Id, Player2Id, Player1Score, Player2Score FROM Matches WHERE Id=?", (match_id,))
                    match_record = cur.fetchall()
                    if len(match_record) > 0:
                        player1_data = cur.execute("SELECT firstname, lastname from players where actual_rank = ?", (match_record[0][1],)).fetchall()
                        player2_data = cur.execute("SELECT firstname, lastname from players where actual_rank = ?", (match_record[0][2],)).fetchall()
                        name1 = player1_data[0][0] + ' ' + player1_data[0][1]
                        name2 = "N/A" if (len(player2_data) < 1) else (player2_data[0][0] + ' ' + player2_data[0][1])
                        score1=match_record[0][3]
                        score2=match_record[0][4]
                    else:
                        name1="N/A"
                        name2="N/A"
                        score1="N/A"
                        score2="N/A"
                elif (matches == 4):
                    external = j + 1
                    p_external = (external + 1) // 2 if external % 2 == 1 else external // 2
                    match_id = str(i + 1) + '.' + str(external)
                    next_round_id = str(i + 2) + '.' + str(p_external)
                    cur.execute("SELECT Id, Player1Id, Player2Id, Player1Score, Player2Score FROM Matches WHERE Id=?", (match_id,))
                    match_record = cur.fetchall()
                    if len(match_record) > 0:
                        player1_data = cur.execute("SELECT firstname, lastname from players where actual_rank = ?", (match_record[0][1],)).fetchall()
                        player2_data = cur.execute("SELECT firstname, lastname from players where actual_rank = ?", (match_record[0][2],)).fetchall()
                        name1 = player1_data[0][0] + ' ' + player1_data[0][1]
                        name2 = "N/A" if (len(player2_data) < 1) else (player2_data[0][0] + ' ' + player2_data[0][1])
                        score1=match_record[0][3]
                        score2=match_record[0][4]
                    else:
                        name1="N/A"
                        name2="N/A"
                        score1="N/A"
                        score2="N/A"
                elif (matches == 2):
                    external = j + 1
                    match_id = str(i + 1) + '.' + str(external)
                    next_round_id = "7.1"
                    cur.execute("SELECT Id, Player1Id, Player2Id, Player1Score, Player2Score FROM Matches WHERE Id=?", (match_id,))
                    match_record = cur.fetchall()
                    if len(match_record) > 0:
                        player1_data = cur.execute("SELECT firstname, lastname from players where actual_rank = ?", (match_record[0][1],)).fetchall()
                        player2_data = cur.execute("SELECT firstname, lastname from players where actual_rank = ?", (match_record[0][2],)).fetchall()
                        name1 = player1_data[0][0] + ' ' + player1_data[0][1]
                        name2 = "N/A" if (len(player2_data) < 1) else (player2_data[0][0] + ' ' + player2_data[0][1])
                        score1=match_record[0][3]
                        score2=match_record[0][4]
                    else:
                        name1="N/A"
                        name2="N/A"
                        score1="N/A"
                        score2="N/A"
                else:
                    match_id = "7.1"
                    cur.execute("SELECT Id, Player1Id, Player2Id, Player1Score, Player2Score FROM Matches WHERE Id=?", (match_id,))
                    match_record = cur.fetchall()
                    if len(match_record) > 0:
                        player1_data = cur.execute("SELECT firstname, lastname from players where actual_rank = ?", (match_record[0][1],)).fetchall()
                        player2_data = cur.execute("SELECT firstname, lastname from players where actual_rank = ?", (match_record[0][2],)).fetchall()
                        name1 = player1_data[0][0] + ' ' + player1_data[0][1]
                        name2 = "N/A" if (len(player2_data) < 1) else (player2_data[0][0] + ' ' + player2_data[0][1])
                        score1=match_record[0][3]
                        score2=match_record[0][4]
                    else:
                        name1="N/A"
                        name2="N/A"
                        score1="N/A"
                        score2="N/A"
                self.create_players_rect(name1, name2, score1, score2, row, column, self.frame.scrollable_frame, i + 1, j + 1,match_id, next_round_id)
                row += add_param
            if (i == 0):
                row = 4
            else:
                row = prev_row + multiplier
                multiplier *= 2
                prev_row = row
            add_param *= 2
            column += 4
        self.frame.pack(fill="both", expand=True)

    def create_draw(self):
        run_draw() # Εκτέλεση κώδικα κλήρωσης από αρχείο draw.py
        self.Exit()
    
    def create_players_rect(self, name1, name2, score1, score2, start_row, start_column, top_1, round_num, match_num, match_id, next_round_id):
        game_title_label = Label(top_1, text=f"ΓΥΡΟΣ: {str(round_num)} ΠΑΙΧΝΙΔΙ: {str(match_num)}")
        game_title_label.configure(font="-family {Poppins SemiBold} -size 12")
        game_title_label.grid(row=start_row, column=start_column)
        player1_name_label = Label(top_1, text=name1)
        player1_name_label.configure(font="-family {Poppins SemiBold} -size 10")
        player1_name_label.grid(row=start_row+1, column=start_column, padx=(20,10))
        player2_name_label = Label(top_1, text=name2)
        player2_name_label.configure(font="-family {Poppins SemiBold} -size 10")
        player2_name_label.grid(row=start_row+2, column=start_column)
        player1_score_label = Label(top_1, text=str(score1))
        player1_score_label.configure(font="-family {Poppins SemiBold} -size 12")
        player1_score_label.grid(row=start_row+1, column=start_column+1)
        player2_score_label = Label(top_1, text=str(score2))
        player2_score_label.configure(font="-family {Poppins SemiBold} -size 12")
        player2_score_label.grid(row=start_row+2, column=start_column+1)
        
        if (name1!="N/A" and name2!="N/A"):
            score_btn = Button(top_1, text="SCORE")
            score_btn.configure(command=lambda match_id=match_id, next_round_id=next_round_id, name1=name1, name2=name2: score_page(match_id, next_round_id, name1, name2))
            score_btn.configure(relief="flat")
            score_btn.configure(overrelief="flat")
            score_btn.configure(activebackground="#CF1E14")
            score_btn.configure(cursor="hand2")
            score_btn.configure(foreground="#ffffff")
            score_btn.configure(background="#CF1E14")
            score_btn.configure(borderwidth="0")
            score_btn.grid(row=start_row, column=start_column+2)

    def Exit(self):
        gamesNoCanvas.destroy()
        root.deiconify()

# Σελίδα καταχώρησης σκορ
class ScoresPage:
    def __init__(self, top=None,match_id=0,next_round_id=0,name1="",name2=""):
        top.geometry("700x350")
        top.resizable(0, 0)
        top.title("AUSTRALIAN OPEN - ΠΛΗΠΡΟ - ΟΜΑΔΑ03 - ΚΑΤΑΧΩΡΗΣΗ ΣΚΟΡ")
        top.protocol('WM_DELETE_WINDOW', self.exit_scores)
        
        self.player1_name_label = Label(scoresPopup)
        self.player1_name_label.place(relx=0.100, rely=0.01)
        self.player1_name_label.configure(font="-family {Poppins SemiBold} -size 15",text=name1)
        
        self.player2_name_label = Label(scoresPopup)
        self.player2_name_label.place(relx=0.400, rely=0.01)
        self.player2_name_label.configure(font="-family {Poppins SemiBold} -size 15",text=name2)

        self.player1_score_entry = Entry(scoresPopup)
        self.player1_score_entry.place(relx=0.100, rely=0.1)
        self.player1_score_entry.configure(font="-family {Poppins SemiBold} -size 15", width=15)

        self.player2_score_entry = Entry(scoresPopup)
        self.player2_score_entry.place(relx=0.400, rely=0.1)
        self.player2_score_entry.configure(font="-family {Poppins SemiBold} -size 15", width=15)

        self.submit_score_btn = Button(scoresPopup)
        self.submit_score_btn.place(relx=0.100, rely=0.2)
        self.submit_score_btn.configure(relief="flat")
        self.submit_score_btn.configure(overrelief="flat")
        self.submit_score_btn.configure(activebackground="#CF1E14")
        self.submit_score_btn.configure(cursor="hand2")
        self.submit_score_btn.configure(foreground="#ffffff")
        self.submit_score_btn.configure(background="#CF1E14")
        self.submit_score_btn.configure(font="-family {Poppins SemiBold} -size 15")
        self.submit_score_btn.configure(borderwidth="0",width=33)
        self.submit_score_btn.configure(text="""ΚΑΤΑΧΩΡΗΣΗ""")
        self.submit_score_btn.configure(command=lambda: self.insert_score(match_id, next_round_id))

        self.fetch_data(match_id)

    def fetch_data(self, match_id):
        current_match = cur.execute('SELECT Id, Player1Id, Player2Id, Player1Score, Player2Score FROM Matches where Id=?', (match_id,)).fetchall()
        if (len(current_match)>0):
            self.player1_score_entry.insert(0, current_match[0][3])
            self.player2_score_entry.insert(0, current_match[0][4])

    def insert_score(self, match_id, next_round_id):
        current_match = cur.execute('SELECT Id, Player1Id, Player2Id, Player1Score, Player2Score FROM Matches where Id=?', (match_id,)).fetchall()
        score1 = self.player1_score_entry.get()
        score2 = self.player2_score_entry.get()
        while not (int(score1) <= 3 and int(score2) <= 3 and int(score1) + int(score2) <= 5):
            messagebox.showerror("ΣΦΑΛΜΑ", "ΜΗ ΑΠΟΔΕΚΤΟ ΣΚΟΡ")
            score1 = self.player1_score_entry.get()
            score2 = self.player2_score_entry.get()
        else: 
            cur.execute('UPDATE Matches SET Player1Score=?, Player2Score=? WHERE Id=?', (int(score1), int(score2), match_id,))
            db.commit()
            winner_id = 0 # Αρχικοποίηση id νικητή
            if int(score1)>int(score2):
                winner_id=int(current_match[0][1]) # Νικητής Player1
            elif int(score1)<int(score2):
                winner_id=int(current_match[0][2])# Νικητής Player2
            else:
                scoresPopup.destroy()
                games_nocanvas_page.deiconify()
            next_match = cur.execute('SELECT Id, Player1Id, Player2Id, Player1Score, Player2Score FROM Matches where Id=?', (next_round_id,)).fetchall()
            if len(next_match) > 0:
                cur.execute("UPDATE Matches SET Player2Id=? WHERE Id=?", (winner_id, next_round_id,))
                db.commit()
            else:
                cur.execute("INSERT INTO Matches (Id, Player1Id,Player1Score, Player2Score) VALUES (?,?,0,0)", (next_round_id,winner_id,))
                db.commit()
            scoresPopup.destroy()
            games_nocanvas_page()
    
    def exit_scores(self):
        scoresPopup.destroy()
        gamesNoCanvas.deiconify()

# Σελίδα Συντελεστές
class AboutPage():
    def __init__(self, top=None):
        top.geometry("700x350")
        top.resizable(0, 0)
        top.title("AUSTRALIAN OPEN - ΠΛΗΠΡΟ - ΟΜΑΔΑ03 - ΣΥΝΤΕΛΕΣΤΕΣ")

        # επιστροφη στο μενου
        self.exit_button = Button(about)
        self.exit_button.place(relx=0.635, rely=0.005, width=200, height=23)
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
        #end region επιστροφη στο μενου
        
        # Συντελεστές         
        self.contributors1_label = Label(about, text="ΓΙΑΝΝΗΣ ΚΑΡΑΜΠΙΝΗΣ")
        self.contributors1_label.configure(font="-family {Poppins SemiBold} -size 10")
        self.contributors1_label.place(relx=0.5, rely=0.1, anchor=CENTER)
        
        self.contributors2_label = Label(about, text="ΑΛΕΞΑΝΔΡΟΣ ΝΑΚΟΣ")
        self.contributors2_label.configure(font="-family {Poppins SemiBold} -size 10")
        self.contributors2_label.place(relx=0.5, rely=0.2, anchor=CENTER)

        self.contributors3_label = Label(about, text="ΕΥΘΥΜΙΟΣ ΓΙΑΛΑΜΑΣ")
        self.contributors3_label.configure(font="-family {Poppins SemiBold} -size 10")
        self.contributors3_label.place(relx=0.5, rely=0.3, anchor=CENTER)

    # Έξοδος από τη σελίδα
    def Exit(self):
        about.destroy()
        root.deiconify()
        
mainPage = MainPage(root)
root.mainloop()
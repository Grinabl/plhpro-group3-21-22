from tkinter import *
from tkinter import ttk
import sqlite3
import os.path
from tkinter import messagebox

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

class MainPage: # Αρχική Σελίδα
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("AUSTRALIAN OPEN - ΠΛΗΠΡΟ - ΟΜΑΔΑ03")

        self.logo_label = Label(root)
        self.logo_label.place(relx=0.85, rely=0.92, width=205, height=60)
        self.logo_label.configure(image=bg)

        self.playersMenuBtn = Button(root)
        self.playersMenuBtn.place(relx=0.14, rely=0, width=250, height=80)
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
        self.gamesMenuBtn.configure(command=players_list)
        

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
        #endregion

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



mainPage = MainPage(root)
root.mainloop()
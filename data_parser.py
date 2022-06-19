import requests
import json
import sqlite3
import os
from tkinter import *
from tkinter.ttk import *

def drop_table_if_exists():
    connection = create_db_connection("database.db")
    cursor = connection.cursor()

    cursor.execute('DROP TABLE IF EXISTS players')
    cursor.execute('DROP TABLE IF EXISTS Matches')

    connection.commit()
    connection.close()

def create_db_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def insert_db_header():
    connection = create_db_connection("database.db")
    cursor = connection.cursor()

    cursor.execute(""" CREATE TABLE IF NOT EXISTS players(firstname text NOT NULL, lastname text NOT NULL,
                    yearofbirth integer NOT NULL, birthplace text NOT NULL, sglrank integer NOT NULL, actual_rank integer NOT NULL); """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS Matches (Id text NOT NULL, Player1Id integer NULL, Player2Id integer NULL, Player1Score integer NOT NULL, Player2Score integer NOT NULL);""")

    connection.commit()
    connection.close()

def update_act_rank():
    connection = create_db_connection("database.db")
    cursor = connection.cursor()

    data = connection.execute("SELECT * FROM players ORDER BY sglrank")

    counter = 1
    for row in data:
        value = int(row[4])
        cursor.execute("""UPDATE players SET actual_rank = ? where sglrank = ?""", (counter, value))
        counter += 1

    connection.commit()
    connection.close()

def data_parsing(window, bar, lbl):
    connection = create_db_connection("database.db")
    cursor = connection.cursor()

    drop_table_if_exists()
    insert_db_header()

    response_API = requests.get('https://ausopen.com/event/195321/players?_format=json')
    data = response_API.text
    players_json = json.loads(data)
    players = players_json['players']

    n_players = len(players)
    for i in range(n_players):
        curr_tour_id = players[i]['tour_id']
        str_curr_tour_id = 'https://ausopen.com/sites/default/files/player_json/' + curr_tour_id + '.json'
        curr_player_API = requests.get(str_curr_tour_id)
        curr_player_data = curr_player_API.text
        curr_player_json = json.loads(curr_player_data)
        firstname = curr_player_json['firstname']
        lastname = curr_player_json['lastname']
        yearofbirth = int(curr_player_json['dob'][0:4])
        birthplace = curr_player_json['birthplace']
        sglrank = int(curr_player_json['sglrank'])
        actual_rank = 1
        cursor.execute("INSERT INTO players VALUES (?, ?, ?, ?, ?, ?)", (firstname, lastname, yearofbirth, birthplace, sglrank, actual_rank))
        connection.commit()
        bar['value'] += 1/n_players * 100
        window.update_idletasks()
        lbl.config(text = "Completed: " + str(round(bar['value'], 2)) + " %")
    update_act_rank()
    connection.close()

def cancel_func(window):
    window.destroy()

def parsing_gui():
    window = Tk()

    window.title('Data Parsing')
    bar = Progressbar(window, orient=HORIZONTAL, length=400)
    bar.pack(padx=20, pady=10)
    lbl = Label(window, text = "")
    lbl.pack(pady = 10)

    button = Button(window, text = "Parse Data", command = lambda: data_parsing(window, bar, lbl)).pack()
    exit_btn = Button(window, text = "Cancel", command = lambda: cancel_func(window)).pack()

    window.mainloop()

if __name__ == '__main__':
    parsing_gui()
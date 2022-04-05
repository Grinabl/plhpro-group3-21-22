import requests
import json
import sqlite3
import os

# First Task: Create Database, Connect with server - fetch required data, Fill the Database, Access The Database

def drop_table_if_exists(connection, cursor):
    cursor.execute('DROP TABLE IF EXISTS players')
    connection.commit()
    print('Previous Table dropped successfully')
    

def create_db_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print('Succesfully connected to database: ' + str(db_file))
        return conn
    except Error as e:
        print(e)
    return conn

def insert_db_header(connection, cursor):
    # Create Table - Players -> Set Header:
    # id integer PRIMARY KEY AUTOINCREMENT
    cursor.execute(""" CREATE TABLE IF NOT EXISTS players(firstname text NOT NULL, lastname text NOT NULL,
                    yearofbirth integer NOT NULL, birthplace text NOT NULL, sglrank integer NOT NULL, actual_rank integer NOT NULL); """)
    connection.commit()

def main():
    connection = create_db_connection("database.db")
    cursor = connection.cursor()

    drop_table_if_exists(connection, cursor)
    insert_db_header(connection, cursor)
    

    # General JSON doesn't have the required data, get tour_ids from general JSON and fetch by tour_id for each player:
    # Fetch all tour_ids for player on men singles:
    response_API = requests.get('https://ausopen.com/event/195321/players?_format=json')
    data = response_API.text
    players_json = json.loads(data)
    players = players_json['players']

    optical_percentage = 0
    n_players = len(players)

    for i in range(n_players):
        curr_tour_id = players[i]['tour_id']
        str_curr_tour_id = 'https://ausopen.com/sites/default/files/player_json/' + curr_tour_id + '.json'
        # JSON for each player, fetched by tour_ids:
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
        optical_percentage += 1/n_players * 100 
        print("%2.2f" % optical_percentage + ' %')

    data = connection.execute("SELECT * FROM players ORDER BY sglrank")

    counter = 1
    for row in data:
        value = int(row[4])
        cursor.execute("""UPDATE players SET actual_rank = ? where sglrank = ?""", (counter, value))
        counter += 1
    connection.commit()
    print("Data parsing completed.\n Database is ready.")
    connection.close()

if __name__ == '__main__':
    main()
    


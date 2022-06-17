import random
import sqlite3
 
# def createPlayers():
#     list = []
#     for i in range(1,129):
#         list.append(i)
#     return list

conn = sqlite3.connect('database.db')
conn.row_factory = lambda cursor, row: row[0]
cur = conn.cursor()
 

playersList = cur.execute("SELECT actual_rank FROM players order by actual_rank asc").fetchall() # get players ids from database table players
rankGroups = [playersList[x:x+16] for x in range(0, len(playersList), 16)]
 
groups = {}
 
 
for i in range(1, 17):
    groups[i] = []
    for j in range(1, 9):
       random.shuffle(rankGroups[j-1])
       player = rankGroups[j-1].pop()
       groups[i].append(player)
print(groups)
 
matches = {}
for i in range(1, 17):
    for j in range(1, 5):
        # matchId = '1.' + str(i) + '.' + str(j)
        matchId = '1.' + str(i) + '.' + str(j)
        random.shuffle(groups[i])
        # cur.execute("""INSERT INTO Matches (Id,Player1Id,Player2Id,Player1Score,Player2Score) VALUES (?,?,?,?,?);""", (matchId, groups[i].pop(), groups[i].pop(), 0, 0))
        # conn.commit()
        matches[matchId] = [groups[i].pop(), groups[i].pop(), 0, 0]
 
print(matches)

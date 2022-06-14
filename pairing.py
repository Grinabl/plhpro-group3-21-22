import sqlite3
import random
from sqlite3 import Error

def dbconnect(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

'''CREATE TABLES OF GROUPS'''
def CreateGroupTable(table_name):
    my_conn = dbconnect("database.db")
    c = my_conn.cursor()
    c.execute(""" CREATE TABLE IF NOT EXISTS {}(firstname text NOT NULL, lastname text NOT NULL,
        yearofbirth integer NOT NULL, birthplace text NOT NULL, actual_rank integer NOT NULL); """.format(table_name))
    my_conn.commit()
    my_conn.close()

def InsertIntoTable(table_name, rank):
    my_conn = dbconnect("database.db")
    c = my_conn.cursor()
    row = c.execute("SELECT * from players WHERE actual_rank={}".format(rank))
    row = row.fetchone()
    print(row)
    firstname = row[0]
    lastname = row[1]
    yearofbirth = row[2]
    birthplace = row[3]
    actual_rank = row[5]
    c.execute("INSERT INTO {} VALUES (?, ?, ?, ?, ?)".format(table_name), (firstname, lastname, yearofbirth, birthplace, actual_rank))
    my_conn.commit()
    my_conn.close()
    
'''SGL_RANK stacks'''
lst_of_stacks = [[i for i in range(1, 17)],
                 [i for i in range(17, 33)],
                 [i for i in range(33, 49)],
                 [i for i in range(49 ,65)],
                 [i for i in range(65, 81)],
                 [i for i in range(81, 97)],
                 [i for i in range(97, 113)],
                 [i for i in range(113, 129)]]

lst_of_groups = []
for i in range(1, 17):
    rand_num_lst = []
    for stack in lst_of_stacks:
        if (len(stack)):
            num = (stack.pop(random.randint(1,100) % len(stack)))
            rand_num_lst.append(num)
        else:
            rand_num_lst.append(stack[0])
    lst_of_groups.append(rand_num_lst)

for i, group in enumerate(lst_of_groups):
    group_name = "Group_{}".format(str(i+1))
    CreateGroupTable(group_name)
    for rank in group:
        InsertIntoTable(group_name, rank)
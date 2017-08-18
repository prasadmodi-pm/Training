import sqlite3
from Sql import createtable,insertinto,connection
def tab(table_name,table_opr):
    table_name = createtable()
   # connection = sqlite3.connect('new.db')
    table_opr = insertinto()
    return table_name,table_opr


tab(table_name='RJP', table_opr=connection.execute("INSERT INTO RJP (SID,SNAME,SAGE,SADDRESS) \
        VALUES (420, 'Paula', 22, 'Texas')"))
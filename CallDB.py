from Sql import createtable, insertinto,connection
from Func import tab

tab(table_name='RJP', table_opr= connection.execute("INSERT INTO RJP (SID,SNAME,SAGE,SADDRESS) \
        VALUES (12, 'Bola', 42, 'NJ')"))

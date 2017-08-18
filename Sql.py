import sqlite3
from sqlite3 import Error

connection = sqlite3.connect('new.db')

print ("open data successfully")

def createtable():


    connection.execute('''CREATE TABLE RJP
         (SID INT PRIMARY KEY     NOT NULL,
         SNAME           TEXT    NOT NULL,
         SAGE            INT     NOT NULL,
         SADDRESS        CHAR(50));''')

createtable()
#print "Table created successfully";

def insertinto():

    connection.execute("INSERT INTO RJP (SID,SNAME,SAGE,SADDRESS) \
        VALUES (10, 'Paul', 32, 'Texas')");

    connection.execute("INSERT INTO RJP (SID,SNAME,SAGE,SADDRESS) \
        VALUES (21, 'Allen', 25, 'Texas')");

    connection.execute("INSERT INTO RJP (SID,SNAME,SAGE,SADDRESS) \
      VALUES (33, 'Teddy', 23, 'New York' )");
insertinto()

def select():
    cursor = connection.execute("SELECT * from RJP")
    for i in cursor:
        print 'SID: ' , i[0]
        print 'SNAME: ', i[1]
        print 'SAGE: ', i[2]
        print 'SADDRESS: ',i[3]

select()


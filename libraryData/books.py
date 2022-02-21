import sqlite3
#connection=sqlite3.connect(':memory:')
connection=sqlite3.connect('books.db')#pass in name of the database that we want to create
cursor=connection.cursor()#create a cursor
#create table
# as it is case sensitive CREATE TABLE  should be capital
#list out the columns and there data type
#if we use single quotation marks " " all columns should be in one line
'''cursor.execute(""" CREATE TABLE listofbooks(
name_of_the_book text,
category text,
author text,
publisher text,
no_of pages integer,
mode text,
published_year integer,
reviews real,
similar_suggestions text,
price real,
)
""") '''#sqlite has only 5 data types they are null,int,real,text,blob --like img ,mp3file it stores exactly what it is

#INSERT DATA ONE BY ONE 
'''cursor.execute(""" INSERT INTO listofbooks VALUES ('IKIGAI',
'STORY',
'HECTOR',
'PENGUINE',
'PURCHASE',
700,
2016,
4.6,
'',600)""")
print("data entered")'''

# INSERT MULTIPLES LINES AT A TIME
"""
many_books=[('our chemical hearts','story','krystal','g.p','read',900,2010,5.0,'',550),
('the gift of imperfection','motivational','brown','hazelden','download',460,2010,3.5,'',860)]
connection.executemany("INSERT INTO listofbooks VALUES(?,?,?,?,?,?,?,?,?,?)",many_books)
print("data inserted")"""

#Query and fetchall
def sug():
     cursor.execute("SELECT* FROM listofbooks    where lib_book_code =1 ")#  * represents every thing

     data = cursor.fetchall()
     print(data)
sug()     
connection.commit() #commit 
connection.close() #close
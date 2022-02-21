from operator import index, indexOf
from flask import Flask
import sqlite3
import os
from flask import request, jsonify


app = Flask(__name__)
file_path = os.path.join(os.getcwd(), 'libraryData','books.db')

connection=sqlite3.connect(file_path)#pass in name of the database that we want to create
cursor=connection.cursor()
cursor.execute("SELECT* FROM listofbooks")
books=cursor.fetchall()
connection.commit()  
connection.close() 

@app.route('/',methods=['Get'])
def hello():
  return 'Hello world from Flask!'
@app.route('/books', methods=['GET'])
def api_all():
    
    if "id" in request.args:
        id = int(request.args['id']) 
    else:
      return jsonify(books)  
    if id==" ":
       return jsonify(books)  

       
    results = []   
    for book in books:
      #checking with index of book in books list and return if id matches with index of book
      '''if id == books.index(book): 
              results.append(book)'''
        #checking with the last element lib_book_code and return if id matches with bookcode        
      '''if id==book[10] : 
              results.append(book) '''
      if id==book[-1]:
                 results.append(book) 
    return jsonify(results)  
app.run()
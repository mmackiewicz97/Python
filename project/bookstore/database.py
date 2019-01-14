import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    #conn=sqlite3.connect("dbname='book' user='postgres' password='123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    #cur.execute("INSERT INTO book VALUES ('%s', '%s', '%s')",%(item, quantity, price))
    #cur.execute("INSERT INTO book VALUES (%s, %s, %s)",(item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn,id))
    conn.commit()
    conn.close()

connect()
#print(view())

#import mysql.connector
#con = mysql.connector.connect(
#    user="ardit700_student", 
#    password = "ardit700_student", 
#    host="108.167.140.122", 
#    database = "ardit700_pm1database"
#)
#cursor = con.cursor()
#query = cursor.execute("SHOW TABLES")
#results = cursor.fetchall()
#print(results)

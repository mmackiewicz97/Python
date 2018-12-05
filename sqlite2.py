import sqlite3
sql = sqlite3.connect("/home/mateusz/Pyton/baza2.sql")
db = sql.cursor()

#DELETE from studenci #usuwa rekordy

# query = 'CREATE TABLE studenci (id, nazwisko, imie, id_studiow)'
# query = 'CREATE TABLE  (id, nazwisko, imie, id_studiow)'
# db.execute(query)
# query ='CREATE TABLE studia(id,studia)'
# db.execute(query)
# query ='CREATE TABLE przedmioty(id,przedmiot)'
# query ='CREATE TABLE przedmioty(id,przedmiot)'
# query ='CREATE TABLE studenci_przedmioty(id,idstudenta, idprzedmiotu)'

# query = 'UPDATE przedmioty SET id=6 WHERE id=7'
# query = 'UPDATE studenci SET id_studiow=NULL WHERE id=8'
# z = db.execute(query)
# print(z.fetchall())
query = "SELECT * FROM studenci ORDER BY 1"
z = db.execute(query)
print(z.fetchall())
query = "SELECT * FROM studia"
z = db.execute(query)
print(z.fetchall())
query = "SELECT * FROM przedmioty"
z = db.execute(query)
print(z.fetchall())
query = "SELECT idstudenta, idprzedmiotu FROM studenci_przedmioty ORDER BY 1"
z = db.execute(query)
print(z.fetchall())
# query = "ALTER TABLE studenci RENAME TO studenci2"
# query = "CREATE TABLE studenci(id, nazwisko, imie)"
# query = 'INSERT INTO studenci(id, nazwisko, imie) SELECT id, nazwisko, imie FROM studenci2 ORDER BY 1'
# query = 'DROP TABLE studenci'
# z = db.execute(query)
# sql.commit()


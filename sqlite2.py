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

# query = 'INSERT INTO studenci(id,nazwisko,imie,id_studiow) values (1, "Kowalski", "Wojtek", 1)'
# query = 'INSERT INTO studenci(id,nazwisko,imie,id_studiow) values (2, "Zawistowski", "Hubert", 1)'
# query = 'INSERT INTO studenci(id,nazwisko,imie,id_studiow) values (3, "Mackiewicz", "Mateusz", 1)'
# query = 'INSERT INTO studia(id,studia) values (1, "SP-PK16")'
# query = 'INSERT INTO studia(id,studia) values (2, "SP-PK17")'
# query = 'INSERT INTO studia(id,studia) values (3, "SP-PK18")'
# query = 'INSERT INTO przedmioty(id,przedmiot) values (1, "matematyka")'
# query = 'INSERT INTO przedmioty(id,przedmiot) values (103, "chemia")'
# query = 'INSERT INTO studenci_przedmioty(id,idstudenta, idprzedmiotu) values (1,8,100)'
# query = 'INSERT INTO studenci_przedmioty(id,idstudenta, idprzedmiotu) values (7,8,101)'
# query = "UPDATE studenci_przedmioty set id=6 WHERE id=7"
# query = 'UPDATE przedmioty set id=6 WHERE id=7'
# query = 'UPDATE studenci set id_studiow=NULL WHERE id=8'
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


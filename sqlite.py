import sqlite3
sql = sqlite3.connect("/home/mateusz/Pyton/baza1.sql")
sql.isolation_level = None
db = sql.cursor()
buffer = ""
# query = 'CREATE TABLE Studenci (id int, imie varchar, nazwisko varchar, odznaka boolean, jakas)'
# query = 'CREATE TABLE Przedmioty (id int, przedmiot_nazwa text)'
# query = "CREATE TABLE Studenci_Przedmioty (id_studenta, id_przedmiotu)"
# query = "CREATE TABLE Oceny (idstudenta, idprzedmiotu, ocena, data)"

# query = "INSERT INTO Studenci (id, imie, nazwisko, odznaka) VALUES (5, 'Ania', 'Nowak', 'True')"
# query = "INSERT INTO Przedmioty (id, przedmiot_nazwa) VALUES (0, 'Matematyka')"
# query = "INSERT INTO Studenci_Przedmioty (id_studenta, id_przedmiotu) VALUES (3,2)"
# query = "INSERT INTO  Oceny VALUES (2,1, 5, '15.10.2018')"

# query = "DROP TABLE ceny" #usunięcie tabeli
# query = "ALTER TABLE Studenci ADD COLUMN jakas"   #dodanie kolumny
# query = "SELECT name FROM sqlite_master WHERE type = 'table'" #.tab
# query = "SELECT sql FROM sqlite_master WHERE type = 'table' " #.schema
# query = "SELECT s.nazwisko, p.przedmiot_nazwa FROM Studenci s, Przedmioty p WHERE s.rowid = 2 AND p.rowid = 3 ORDER BY s.rowid"
# query = "SELECT AVG(OCENA) FROM Oceny WHERE idprzedmiotu IN (1,2)"
# query = "SELECT Ocena, nazwisko FROM (Oceny o JOIN Studenci s ON o.idstudenta = s.id)"
# query = 'SELECT a.id, a.nazwisko, b.nazwisko FROM Studenci a, Studenci b WHERE a.id = b.id'
# query = 'SELECT * FROM Studenci LIMIT 2'
# query = 'SELECT * FROM Oceny WHERE data BETWEEN "14-10-2018" AND "16-10-2018"'
# query = 'UPDATE przedmioty SET id=6 WHERE id=7'
# query = 'DELETE FROM Przedmioty WHERE przedmiot_nazwa = "Matematyka"'
# query = 'CREATE TABLE jakas AS SELECT * FROM inna'
# query = 'INSERT INTO jakas (kolumna1, kolumna2) SELECT kolumna1, kolumna2 FROM inna'
# ORDER BY kolumn, DESC, ASDESC
# GROUP BY 1, imie,
# WHERE nazwisko LIKE 'sz%' # %-zero, one or multiple characters; _-the underscore represents a single character LIKE '_r%a'
# LIKE '[a-c]%' '[!0-9]%'
# WHERE IN (1,2) IN (SELECT ...)
# AND; OR; NOT;
# IS NULL; IS NOT NULL, ANY, ALL
# MIN(); MAX(); COUNT(); AVG(); SUM();
# sql.commit()

# query = "CREATE TABLE Orders (ID int PRIMARY KEY, OrderNumber int NOT NULL, OrderDate date DEFAULT (datetime('now', 'localtime')))"
# query = 'SELECT rowid, OrderNumber, OrderDate FROM Orders WHERE OrderDate>"2018-12-01 14:13:50"'
# query = "CREATE VIEW [Students] AS SELECT imie, nazwisko FROM Studenci"
# query = "SELECT * FROM [Students]"
z = db.execute('SELECT REPLACE(nazwisko, "owak", "owakowski") FROM Studenci WHERE nazwisko LIKE "%owak"')
# print(z.fetchall())
# sql.commit()
print(z.fetchall())
query = "SELECT przedmiot_nazwa, nazwisko, ocena FROM Oceny, Studenci, Przedmioty WHERE Oceny.idstudenta = Studenci.id AND Oceny.idprzedmiotu = Przedmioty.id"
z = db.execute(query)
print(z.fetchall())
query = "SELECT przedmiot_nazwa, nazwisko, AVG(ocena) FROM Oceny, Studenci, Przedmioty WHERE Oceny.idstudenta = Studenci.id AND Oceny.idprzedmiotu = Przedmioty.id GROUP BY nazwisko, przedmiot_nazwa ORDER BY przedmiot_nazwa"
z = db.execute(query)
print(z.fetchall())
query = "SELECT * FROM Studenci"
z = db.execute(query)
print("SELECT * FROM Studenci:", z.fetchall())

query = "SELECT * FROM Oceny"
z = db.execute(query)
print("SELECT * FROM Oceny:", z.fetchall())

query = "SELECT * FROM Przedmioty"
z = db.execute(query)
print("SELECT * FROM Przedmioty:", z.fetchall())

query = "SELECT * FROM Studenci_Przedmioty"
z = db.execute(query)
print("SELECT * FROM Studenci_Przedmioty:", z.fetchall())
print("Enter your SQL commands to execute in sqlite3.")
print ("Enter a blank line to exit.")

while True:
    line = input()
    if line == "":
        break
    buffer += line
    if sqlite3.complete_statement(buffer):
        try:
            buffer = buffer.strip()
            db.execute(buffer)

            if buffer.lstrip().upper().startswith("SELECT"):
                print(db.fetchall())
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
        buffer = ""

sql.close()
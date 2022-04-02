import sqlite3
conn = sqlite3.connect('school.db')
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS classes")
cur.execute("DROP TABLE IF EXISTS students")

query = "CREATE TABLE IF NOT EXISTS classes (Id INT, class INT, num_of_stud INT, teacher TEXT)"
cur.execute(query)
cur.execute("INSERT INTO classes VALUES(1, 7, 20, 'Ivanova')")
cur.execute("INSERT INTO classes VALUES(2, 8, 24, 'Petrova')")
cur.execute("INSERT INTO classes VALUES(3, 9, 30, 'Mihaylovna')")
cur.execute("INSERT INTO classes VALUES(4, 10, 32, 'Vladimirovna')")
cur.execute("INSERT INTO classes VALUES(5, 11, 25, 'Vasylevna')")

query1 = "CREATE TABLE IF NOT EXISTS students (id INT, familia TEXT, imya TEXT, otchestvo TEXT, class INT, hobby)"
cur.execute(query1)
cur.execute("INSERT INTO students VALUES(1, 'Semenov', 'Fedor', 'Vladimirovich', 7, 'football')")
cur.execute("INSERT INTO students VALUES(2, 'Sivov', 'Maxim', 'Egorovich', 8, 'reading')")
cur.execute("INSERT INTO students VALUES(3, 'Ushinskii', 'Petr', 'Vyacheslavovich', 7, 'programmer')")
cur.execute("INSERT INTO students VALUES(4, 'Alimov', 'Alexander', 'Denisovich', 10, 'eating')")
cur.execute("INSERT INTO students VALUES(5, 'Maria', 'Vostrova', 'Alexandrovna', 7, 'computer games')")

cur.execute("SELECT class, num_of_stud FROM classes")
rows = cur.fetchall()
for row in rows:
    print(row)
print('--------------------------------')
cur.execute("SELECT * FROM students")
rows = cur.fetchall()
for row in rows:
    print(row)
print('--------------------------------')
cur.execute("SELECT * FROM students WHERE imya = 'Petr'")
rows = cur.fetchall()
for row in rows:
    print(row)
print('--------------------------------')
cur.execute("SELECT class FROM classes WHERE num_of_stud>=25")
rows = cur.fetchall()
for row in rows:
    print(row)

conn.commit()
conn.close()

import sqlite3

conn = sqlite3.connect('school.db')
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS classes")
cur.execute("DROP TABLE IF EXISTS students")
cur.execute("DROP TABLE IF EXISTS subjects")
cur.execute("DROP TABLE IF EXISTS marks")

cur.execute("PRAGMA foreign_keys = ON")

query = "CREATE TABLE IF NOT EXISTS classes (id INT NOT NULL PRIMARY KEY, class INT, num_of_stud INT, teacher TEXT)"
cur.execute(query)
cur.execute("INSERT INTO classes VALUES(1, 7, 20, 'Ivanova')")
cur.execute("INSERT INTO classes VALUES(2, 8, 24, 'Petrova')")
cur.execute("INSERT INTO classes VALUES(3, 9, 30, 'Mihaylovna')")
cur.execute("INSERT INTO classes VALUES(4, 10, 32, 'Vladimirovna')")
cur.execute("INSERT INTO classes VALUES(5, 11, 25, 'Vasylevna')")

query1 = "CREATE TABLE IF NOT EXISTS students (id INT NOT NULL PRIMARY KEY, familia TEXT, imya TEXT, otchestvo TEXT, id_classes INT, age INT, gender TEXT, FOREIGN KEY (id_classes) REFERENCES classes (id) ON UPDATE CASCADE)"
cur.execute(query1)
cur.execute("INSERT INTO students VALUES(01, 'Semenov', 'Fedor', 'Vladimirovich', 1, 14, 'male')")
cur.execute("INSERT INTO students VALUES(02, 'Sivov', 'Maxim', 'Egorovich', 2, 16, 'male')")
cur.execute("INSERT INTO students VALUES(03, 'Ushinskii', 'Petr', 'Vyacheslavovich', 3, 15, 'male')")
cur.execute("INSERT INTO students VALUES(04, 'Alimov', 'Alexander', 'Denisovich', 4, 16, 'male')")
cur.execute("INSERT INTO students VALUES(05, 'Maria', 'Vostrova', 'Alexandrovna', 5, 14, 'female')")

query2 = "CREATE TABLE IF NOT EXISTS subjects (id INT NOT NULL PRIMARY KEY, subject)"
cur.execute(query2)
cur.execute("INSERT INTO subjects VALUES(001, 'RussianLanguage')")
cur.execute("INSERT INTO subjects VALUES(002, 'EnglishLanguage')")
cur.execute("INSERT INTO subjects VALUES(003, 'Math')")
cur.execute("INSERT INTO subjects VALUES(004, 'Biology')")
cur.execute("INSERT INTO subjects VALUES(005, 'Geography')")

query3 = "CREATE TABLE IF NOT EXISTS marks (id INT NOT NULL PRIMARY KEY, mark INT, id_students INT, id_subjects INT, FOREIGN KEY (id_subjects) REFERENCES subjects(id) ON UPDATE CASCADE, FOREIGN KEY (id_students) REFERENCES students(id) ON UPDATE CASCADE)"
cur.execute(query3)
cur.execute("INSERT INTO marks VALUES(0001, 5, 1, 001)")
cur.execute("INSERT INTO marks VALUES(0002, 4, 2, 002)")
cur.execute("INSERT INTO marks VALUES(0003, 5, 3, 003)")
cur.execute("INSERT INTO marks VALUES(0004, 2, 4, 004)")
cur.execute("INSERT INTO marks VALUES(0005, 3, 5, 005)")

cur.execute("SELECT * FROM classes")
rows = cur.fetchall()
for row in rows:
    print(row)
print('--------------------------------')
cur.execute("SELECT * FROM students")
rows = cur.fetchall()
for row in rows:
    print(row)
print('--------------------------------')
cur.execute("SELECT * FROM subjects")
rows = cur.fetchall()
for row in rows:
    print(row)
print('--------------------------------')
cur.execute("SELECT * FROM marks")
rows = cur.fetchall()
for row in rows:
    print(row)
print('--------------------------------')

conn.commit()
conn.close()
import sqlite3
conn = sqlite3.connect('basadate.db')
cursor = conn.cursor()
#cursor.execute('DROP TABLE IF EXISTS  book_in_library')
#cursor.execute('DROP TABLE IF EXISTS  take_a_book')
#cursor.execute('DROP TABLE IF EXISTS  student')
#cursor.execute('DROP TABLE IF EXISTS  book')
#cursor.execute('DROP TABLE IF EXISTS  library')

cursor.execute('''CREATE TABLE IF NOT EXISTS student
            	(id_student INTEGER PRIMARY KEY, 
            	name TEXT NOT NULL, 
            	surname TEXT NOT NULL,
            	age INTEGER NOT NULL,
            	course INTEGER NOT NULL,
            	faculty TEXT NOT NULL);''')

cursor.execute('''CREATE TABLE  IF NOT EXISTS  book
            	(id_book INTEGER PRIMARY KEY NOT NULL, 
            	name_book TEXT NOT NULL, 
            	author TEXT NOT NULL,
            	year_of_publication INTEGER );''')

cursor.execute('''CREATE TABLE  IF NOT EXISTS  library
            	(id_library INTEGER PRIMARY KEY , 
            	name_library TEXT NOT NULL, 
            	address_library INTEGER NOT NULL);''')

cursor.execute('''CREATE TABLE  IF NOT EXISTS  book_in_library
            	( id_book_in_library INTEGER PRIMARY KEY,
            	copies INTEGER,
            	id_books INTEGER,
            	id_libraryes INTEGER,
            	FOREIGN KEY (id_books) REFERENCES book(id_book), 
            	FOREIGN KEY (id_libraryes) REFERENCES library(id_library));''')

cursor.execute('''CREATE TABLE IF NOT EXISTS  take_a_book
            	( id_take INTEGER PRIMARY KEY,
            	number_of_days INTEGER,
            	id1_books INTEGER,
            	id1_students INTEGER,
            	FOREIGN KEY (id1_books) REFERENCES book(id_book), 
            	FOREIGN KEY (id1_students) REFERENCES student(id_student));''')

conn.commit()
cursor.execute("""INSERT INTO student(id_student, name, surname, age, course,faculty) 
   VALUES('11', 'Александр','Невский', '20', '2','Исторический');""")
cursor.execute("""INSERT INTO student(id_student, name, surname, age, course,faculty) 
   VALUES('12', 'Дмитрий','Менделеев', '21', '3','Химический');""")



cursor.execute("""INSERT INTO book(id_book, name_book , author ,year_of_publication)
   VALUES('21', 'Ромео и Джульетта','Шекспир','1869');""")
cursor.execute("""INSERT INTO book(id_book, name_book ,author , year_of_publication)
   VALUES('22', 'Герой нашего времени','Лермонтов','1840');""")

cursor.execute("""INSERT INTO library(id_library, name_library , address_library)
   VALUES('31', 'Библиотека имени Ленина','Москва, ул.Воздвиженка');""")
cursor.execute("""INSERT INTO library(id_library, name_library , address_library)
   VALUES('32', 'Библиотека имени Ломоносова','Санкт-Петербург, ул Нахимова');""")


cursor.execute("""INSERT INTO book_in_library(id_book_in_library, copies,id_books,id_libraryes)
   VALUES('41', '1000', '21','31' );""")
cursor.execute("""INSERT INTO book_in_library(id_book_in_library, copies,id_books,id_libraryes)
   VALUES('42', '200', '22','31' );""")

cursor.execute("""INSERT INTO  take_a_book(id_take , number_of_days,id1_books,id1_students)
   VALUES('51', '10', '21','11' );""")
cursor.execute("""INSERT INTO  take_a_book(id_take , number_of_days,id1_books,id1_students)
   VALUES('52', '7', '22','12' );""")
cursor.execute("""INSERT INTO  take_a_book(id_take , number_of_days,id1_books,id1_students)
   VALUES('53', '15', '21','11' );""")

conn.commit()
sqlite_select_query ="""Select* from student;"""





cursor.execute(sqlite_select_query)
records = cursor.fetchall()
print("Всего строк:  ", len(records))
print("Вывод каждой строки")
for row in records:
    print("ID:", row[0])
    print("Имя:", row[1])
    print("Фамилия:", row[2])
    print("Возраст:", row[3])
    print("Курс:", row[4])
    print("Факультет:", row[5], end="\n\n")

sqlite_select_query ="""Select id1_books,name,surname from take_a_book,student where student.id_student=take_a_book.id1_students and student.surname="Менделеев";"""

cursor.execute(sqlite_select_query)
records = cursor.fetchall()
print("Всего строк:  ", len(records))
print("Вывод книг, которые брал  Дмитрий Менделеев ")
for row in records:
    print("ID book:", row[0])
    print("Имя студента:", row[1])
    print("Фамилия студента:", row[2], end="\n\n")



sqlite_select_query ="""Select* from student  where course=2;"""

cursor.execute(sqlite_select_query)
records = cursor.fetchall()
print("Всего строк:  ", len(records))
print("Вывод студентов 2 курса")
for row in records:
    print("ID:", row[0])
    print("Имя:", row[1])
    print("Фамилия:", row[2])
    print("Возраст:", row[3])
    print("Факультет:", row[5], end="\n\n")
cursor.execute('SELECT MAX(age) FROM student')

min_age = cursor.fetchone()[0]
print('Возраст самого взрослого студента:', min_age)


conn.close()
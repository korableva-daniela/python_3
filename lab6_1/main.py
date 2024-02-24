import sqlite3
conn = sqlite3.connect('basadate.db')
cursor = conn.cursor()

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
            	( id_book_in_library INTEGER,
            	copies INTEGER,
            	id_books INTEGER,
            	id_libraryes INTEGER,
            	FOREIGN KEY (id_books) REFERENCES book(id_book), 
            	FOREIGN KEY (id_libraryes) REFERENCES library(id_library));''')

cursor.execute('''CREATE TABLE IF NOT EXISTS  take_a_book
            	( id_take INTEGER,
            	number_of_days INTEGER,
            	id_books INTEGER,
            	id_students INTEGER,
            	FOREIGN KEY (id_books) REFERENCES book(id_book), 
            	FOREIGN KEY (id_students) REFERENCES student(id_student));''')

conn.commit()
cursor.execute("""INSERT INTO student(id_student, name, surname, age, course,faculty) 
   VALUES('00001', 'Александр','Невский', '20', '2','Исторический');""")
cursor.execute("""INSERT INTO student(id_student, name, surname, age, course,faculty) 
   VALUES('00002', 'Дмитрий','Менделеев', '21', '3','Химический');""")



cursor.execute("""INSERT INTO book(id_book, name_book , author ,year_of_publication)
   VALUES('00011', 'Ромео и Джульетта','Шекспир','1869');""")
cursor.execute("""INSERT INTO book(id_book, name_book ,author , year_of_publication)
   VALUES('00012', 'Герой нашего времени','Лермонтов','1840');""")

cursor.execute("""INSERT INTO library(id_library, name_library , address_library)
   VALUES('00111', 'Библиотека имени Ленина','Москва, ул.Воздвиженка');""")
cursor.execute("""INSERT INTO library(id_library, name_library , address_library)
   VALUES('00222', 'Библиотека имени Ломоносова','Санкт-Петербург, ул Нахимова');""")


cursor.execute("""INSERT INTO book_in_library(id_book_in_library, copies,id_books,id_libraryes)
   VALUES('01111', '1000', '00011','00222' );""")
cursor.execute("""INSERT INTO book_in_library(id_book_in_library, copies,id_books,id_libraryes)
   VALUES('02222', '200', '00012','00111' );""")

cursor.execute("""INSERT INTO  take_a_book(id_take , number_of_days,id_books,id_students)
   VALUES('11111', '10', '00011','00002' );""")
cursor.execute("""INSERT INTO  take_a_book(id_take , number_of_days,id_books,id_students)
   VALUES('22222', '7', '00012','00001' );""")
cursor.execute("""INSERT INTO  take_a_book(id_take , number_of_days,id_books,id_students)
   VALUES('33333', '15', '00012','00002' );""")

sqlite_select_query ="""Select* from student;"""

conn.commit()





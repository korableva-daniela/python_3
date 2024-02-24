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

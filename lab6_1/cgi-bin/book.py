# -*- coding: utf-8 -*-
#!/usr/bin/env python
import cgi
import cgitb; cgitb.enable()
import html
import sqlite3

print("Content-type: text/html\n")
form =cgi.FieldStorage()
text1 = form.getfirst("name_book","не задано")
text2 = form.getfirst("author", "не задано")
text3 = form.getfirst("year_of_publication", "не задано")

text1=html.escape(text1)
text2=html.escape(text2)
text3=html.escape(text3)
try:
    conn = sqlite3.connect('basadate.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO book (name_book, author, year_of_publication) 
                      VALUES (?, ?, ?)''', (text1, text2, text3))
    conn.commit()
    print('<html>')
    print('<head>')
    print('<title> Python on a web server</title>')
    print('<meta content="text/html;charset=utf-8" http-equiv="Content-Type">')
    print(' <meta name="viewport" content="width=device-width initial-scale=1,shrink-to-fit=no">')
    print('<link rel="stylesheet" href="style.css">')
    print('</head>')
    print('<body>')

    print('<h2>Новая книга:</h2>', '<br /><br />')
    print('</body>')
    print('</html>')
    print("<p>Название:", text1)
    print("<p>Автор:", text2)
    print("<p>Год издания:", text3)

    print ('</body>')
    print ('</html>')
except sqlite3.Error as e:
    print("<p>Error: {}</p>".format(e))
finally:
    if conn:
        conn.close()
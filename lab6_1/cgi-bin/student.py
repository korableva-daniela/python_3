# -*- coding: utf-8 -*-
#!/usr/bin/env python
import cgi
import cgitb; cgitb.enable()
import html
import sqlite3
print("Content-type: text/html\n")
form =cgi.FieldStorage()
text1 = form.getfirst("name","не задано")
text2 = form.getfirst("surname", "не задано")
text3 = form.getfirst("age", "не задано")
text4 = form.getfirst("course", "не задано")
text5 = form.getfirst("faculty", "не задано")
text1=html.escape(text1)
text2=html.escape(text2)
text3=html.escape(text3)
text4=html.escape(text4)
text5=html.escape(text5)
try:
    conn = sqlite3.connect('basadate.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO student (name, surname, age,course,faculty) 
                      VALUES (?, ?, ?, ?, ?)''', (text1, text2, text3,text4,text5))
    conn.commit()
    print('<html>')
    print('<head>')
    print('<title> Python on a web server</title>')
    print('<meta content="text/html;charset=utf-8" http-equiv="Content-Type">')
    print(' <meta name="viewport" content="width=device-width initial-scale=1,shrink-to-fit=no">')
    print('<link rel="stylesheet" href="style.css">')
    print('</head>')
    print('<body>')

    print('<h2>Новый студент:</h2>', '<br /><br />')
    print('</body>')
    print('</html>')
    print("<p>Имя:", text1)
    print("<p>Фамилия:", text2)
    print("<p>Возраст:", text3)
    print("<p>Курс:", text4)
    print("<p>Факультет:",text5)
    print ('</body>')
    print ('</html>')
except sqlite3.Error as e:
    print("<p>Error: {}</p>".format(e))
finally:
    if conn:
        conn.close()
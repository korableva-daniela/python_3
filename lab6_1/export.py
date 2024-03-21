import sqlite3
import json
data = []

def addData(tablename):
    conn = sqlite3.connect('basadate.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {tablename}")
    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    data = []
    for row in rows:
        data.append(dict(zip(columns, row)))
    conn.close()
    return data
data.append(addData("student"))
data.append(addData(" book"))
data.append(addData("library"))
data.append(addData("book_in_library"))
data.append(addData(" take_a_book"))
with open('developers.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
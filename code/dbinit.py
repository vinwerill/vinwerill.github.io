import os
# try:
os.unlink('library.db')
# except:
#     print('首次建檔')


def show_all_rows(all_rows):
    for row in all_rows:
        print(row)
    print()

import sqlite3
conn = sqlite3.connect('library.db')
cur = conn.cursor()

cur.execute(''' CREATE TABLE USERS
(ID integer, NAME text, AGE integer, BORROW_QUANTITY integer)''')

cur.execute("INSERT INTO USERS VALUES (1, 'John', 18, 20)")
cur.execute("INSERT INTO USERS VALUES (2, 'Jane', 20, 20)")

cur.execute(''' CREATE TABLE BOOKS
(ID integer, BNAME text, WRITER text, CODE text)''')

cur.execute('''CREATE TABLE BORROWED_BOOK
(USER TEXT, BOOK TEXT)''')

row_id = 0
fin = open('library-books.txt', 'rt', encoding='utf-8')
lines = fin.readlines()
for line in lines:
    row_id += 1
    word = (line.strip('\n')).split(' ')
    cur.execute("INSERT INTO BOOKS VALUES (?, ?, ?, ?)", (row_id, word[0],word[1], word[2]))
conn.commit()    
fin.close()

cur.execute('SELECT * FROM BOOKS')
show_all_rows(cur.fetchall())

cur.execute('SELECT * FROM USERS')
show_all_rows(cur.fetchall())





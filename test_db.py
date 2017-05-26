# coding=gbk
__author__ = 'RobinLin'



import re

msg = '消费12.5'
cost_str = msg[2:]
cost_value = 0.0
try:
    cost_value = float(cost_str)
except:
    cost_value = 0.0
print(cost_value)
#
# import sqlite3
#
# conn = sqlite3.connect("test.db")
# c = conn.cursor()
#
# books = [(1, 1, 'Cook Recipe', 3.12, 1),
#          (2, 3, 'Python Intro', 17.5, 2),
#          (3, 2, 'OS Intro', 13.6, 2),
#          ]
# # create tables
# c.execute('''CREATE TABLE category
#       (id int primary key, sort int, name text)''')
# c.execute('''CREATE TABLE book
#       (id int primary key,
#        sort int,
#        name text,
#        price real,
#        category int,
#        FOREIGN KEY (category) REFERENCES category(id))''')
#
# # save the changes
# conn.commit()

# # execute "INSERT"
# c.execute("INSERT INTO category VALUES (1, 1, 'kitchen')")
#
# # using the placeholder
# c.execute("INSERT INTO category VALUES (?, ?, ?)", (2, 2, 'computer'))
#
# # execute multiple commands
# c.executemany('INSERT INTO book VALUES (?, ?, ?, ?, ?)', books)

# retrieve one record
# c.execute('SELECT name FROM category ORDER BY sort')
# print(c.fetchone())
# print(c.fetchone())

# retrieve all records as a list
# c.execute('SELECT * FROM book WHERE book.category=1')
# print(c.fetchall())
#
# # iterate through the records
# for row in c.execute('SELECT name, price FROM book ORDER BY sort'):
#     print(type(row))

# conn.commit()
# conn.close()
import sqlite3
import random

conn = sqlite3.connect('core.db')
c = conn.cursor()

def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS core(id INTEGER, name TEXT, age INTEGER, birthdate TEXT, gender TEXT)")

def data_entry():
	c.execute("INSERT INTO core VALUES(20, '2010-2-3', 'python', 5)")
	conn.commit()
	c.close()
	conn.close()

create_table()
data_entry()


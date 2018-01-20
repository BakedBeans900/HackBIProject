import sqlite3
import random

conn = sqlite3.connect('test.db')
c = conn.cursor()

def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS test(unix REAL, datestamp TEXT, keyword TEXT, Value REAL)")

def data_entry():
	c.execute("INSERT INTO test VALUES(20, '2010-2-3', 'python', 5)")
	conn.commit()
	c.close()
	conn.close()

create_table()
data_entry()


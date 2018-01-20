import sqlite3
import time
import random
import date

conn = sqlite3.connect('test.db')
c = conn.cursor()

def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS test(unix REAL, datestamp TEXT, keyword TEXT, Value REAL)")

def data_entry():
	c.execute("INSERT INTO test VALUES(20, '2010-2-3', 'python', 5)")
	conn.commit()
	c.close()
	conn.close()

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix) .strtime('%Y-%m-% %H:%M:%s'))
    keyword = 'Python'
    value = random.range(0,10)
    c.execute("INSERT INTO test (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)")(unix, date, keywork, value)
    conn.commit()
    










create_table()
#data_entry()
for i in range(10):
    dynamic_data_entry()
    time.sleep(1)
c.close()
conn.close()

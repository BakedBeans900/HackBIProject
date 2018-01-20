import sqlite3

conn = sqlite3.connect('core.db')
c = conn.cursor()

def create_table(table_name, cols):
        """Creates a table 'core' if there already isnt one"""
        c.execute("CREATE TABLE IF NOT EXISTS " + table_name + "(" + cols + ")")
	
def data_entry(name=, age, birthdate, gender):
        """enter parameters to make a new entry on the database"""
        conn = sqlite3.connect('core.db')
        c = conn.cursor()
        c.execute("INSERT INTO core (name, age, birthdate, gender) VALUES (?, ?, ?, ?)",(name, age, birthdate, gender))
        conn.commit()
        conn.close()

def data_lookup(name):
        """Enter the name, returns a tuple with the data"""
        results = c.execute("SELECT * FROM core WHERE name LIKE " + "\"" + name + "\"")
        data = results.fetchall()
        return data


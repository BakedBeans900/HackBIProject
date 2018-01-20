import sqlite3

conn = sqlite3.connect('core.db')
c = conn.cursor()

#Create a table with given columns. Example: "name TEXT, age INTEGER, birthdate TEXT, gender TEXT"
def create_table(table_name, cols):
        """Creates a table if there already isnt one"""
        c.execute("CREATE TABLE IF NOT EXISTS " + table_name + "(" + cols + ")")


def add_profile_entry(name, age, birthdate, gender, crime, priority):
        """enter parameters to make a new entry on the database"""
        conn = sqlite3.connect('core.db')
        c = conn.cursor()
        if data_lookup_profile(name): #checks to see if the person is in there by checking if the list returned by data_lookup isn't empty
                old_name = str((data_lookup_profile(name))[0])
                print(old_name)
                print(data_lookup_profile(name)[0])
                c.execute("UPDATE core SET age=" + str(age) + " WHERE name=\"" + old_name + "\"")
                c.execute("UPDATE core SET birthdate=\"" + birthdate + "\" WHERE name=\"" + old_name + "\"")
                c.execute("UPDATE core SET gender=\"" + gender + "\" WHERE name=\"" + old_name + "\"")
                c.execute("UPDATE core SET crime=\"" + crime + "\" WHERE name=\"" + old_name + "\"")
                c.execute("UPDATE core SET priority=" + str(priority) + " WHERE name=\"" + old_name + "\"")
                conn.commit()
        else:
                c.execute("INSERT INTO core (name, age, birthdate, gender, crime, priority) VALUES (?, ?, ?, ?, ?, ?)",(name, age, birthdate, gender, crime, priority))
        conn.commit()
        conn.close()

def data_lookup_profile(name):
        """Enter the name, returns a tuple with the data"""
        results = c.execute("SELECT * FROM core WHERE name LIKE " + "\"" + name + "\"")
        data = results.fetchall()[0]
        print(data[0])
        return data

def core_print_all():
        conn = sqlite3.connect('core.db')
        c = conn.cursor()
        stuff = c.execute("SELECT * FROM core")
        print(stuff.fetchall())
        conn.close()


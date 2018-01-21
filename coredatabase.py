import sqlite3
#database name:core, table names:profiles, matching_logs

conn = sqlite3.connect('core.db')
c = conn.cursor()

#Create a table with given columns. Example: "name TEXT, age INTEGER, birthdate TEXT, gender TEXT"
def create_table(table_name, cols):
        """Creates a table if there already isnt one"""
        conn = sqlite3.connect('core.db')
        c = conn.cursor()s
        c.execute("CREATE TABLE IF NOT EXISTS " + table_name + "(" + cols + ")")




def add_profile_entry(name, age, birthdate, gender, crime, priority, images_path):
        """enter parameters to make a new entry on the database"""
        conn = sqlite3.connect('core.db')
        c = conn.cursor()
        if data_lookup_profile(name): #checks to see if the person is in there by checking if the list returned by data_lookup isn't empty
                old_name = data_lookup_profile(name)[0]
                c.execute("UPDATE profiles SET age=" + str(age) + " WHERE name=\"" + old_name + "\"")
                c.execute("UPDATE profiles SET birthdate=\"" + birthdate + "\" WHERE name=\"" + old_name + "\"")
                c.execute("UPDATE profiles SET gender=\"" + gender + "\" WHERE name=\"" + old_name + "\"")
                c.execute("UPDATE profiles SET crime=\"" + crime + "\" WHERE name=\"" + old_name + "\"")
                c.execute("UPDATE profiles SET priority=" + str(priority) + " WHERE name=\"" + old_name + "\"")
                c.execute("UPDATE profiles SET images_path=\"" + images_path + "\" WHERE name=\"" + old_name + "\"")
        else:
                c.execute("INSERT INTO profiles (name, age, birthdate, gender, crime, priority, images_path) VALUES (?, ?, ?, ?, ?, ?, ?)",(name, age, birthdate, gender, crime, priority, images_path))
        conn.commit()
        c.close()
        conn.close()

def add_matching_logs(time, location, name):
        conn = sqlite3.connect('core.db')
        c = conn.cursor()
        c.execute("INSERT INTO matching_logs (time, location, name) VALUES (?, ?, ?)", (time, location, name))
        c.close()
        conn.commit()
        conn.close()

def data_lookup_profile(name):
        """Enter the name, returns a tuple with the data"""
        conn = sqlite3.connect('core.db')
        c = conn.cursor()
        results = c.execute("SELECT * FROM profiles WHERE name LIKE " + "\"" + name + "\"")
        data = ()
        try:
                data = results.fetchall()[0]
        except:
                pass
        return data

def location_logs(location):
        conn = sqlite3.connect('core.db')
        c = conn.cursor()
        logs = c.execute("SELECT * FROM matching_logs WHERE location=\"" + location + "\"")
        return logs.fetchall()

def return_all_profiles():
        conn = sqlite3.connect('core.db')
        c = conn.cursor()
        stuff = c.execute("SELECT * FROM profiles")
        stuff = stuff.fetchall()
        return stuff
        conn.close()


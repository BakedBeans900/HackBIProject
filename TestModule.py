import sqlite3
import coredatabase

coredatabase.create_table("core", "name TEXT, age INTEGER, birthdate TEXT, gender TEXT")
coredatabase.data_entry("Darold", 20, "1/1/1999", "Male")
x = coredatabase.data_lookup("Darold")
print(x)

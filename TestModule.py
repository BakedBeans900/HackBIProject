import sqlite3
import coredatabase

coredatabase.create_table("core", "name TEXT, age INTEGER, birthdate TEXT, gender TEXT, crime TEXT, priority INTEGER")
coredatabase.add_profile_entry("Darold", 19, "1/1/1999", "Male", "None", 1)
coredatabase.core_print_all()

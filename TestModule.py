import sqlite3
import coredatabase

coredatabase.create_table("profiles", "name TEXT, age INTEGER, birthdate TEXT, gender TEXT, crime TEXT, priority INTEGER, images_path TEXT")
coredatabase.add_profile_entry("Darold", 20, "1/1/1999", "Male", "None", 1, "Darold")
coredatabase.create_table("matching_logs", "time TEXT, location TEXT, name TEXT")
coredatabase.add_matching_logs("7am", "Olney", "Darold")
coredatabase.add_matching_logs("9am", "Olney", "Bob")
print(coredatabase.location_logs("Olney"))
print(coredatabase.return_all_profiles())

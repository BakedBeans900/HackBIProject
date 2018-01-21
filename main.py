#Main.py
import facialRecognition as fR
import coredatabase as cdb
import time
import os

profile_folder_path = os.getcwd() + "/profile_images"
cdb.create_table("profiles", "name TEXT, age INTEGER, birthdate TEXT, crime TEXT, priority INTEGER, images_path TEXT")
cdb.create_table("matching_logs", "time TEXT, location TEXT, name TEXT")
fR.trainRecognizer(profile_folder_path)
os.chdir('..')
for input_image_name in os.listdir(os.getcwd() + "/raw_images"):
    matched = fR.match(os.getcwd() + "/raw_images", input_image_name)
    for match in matched:
        local_time = time.asctime(time.localtime(time.time()))
        cdb.add_matching_logs(local_time, "BI", match)
    shutil(os.getcwd() + "raw_images/" + input_image_name, os.getcwd() + "processed_images/" + input_image_name)

for lo in location_logs("BI"):
    print(lo)


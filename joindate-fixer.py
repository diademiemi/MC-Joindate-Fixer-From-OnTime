#!/usr/bin/env python3

# firstPlayed in player.dat file fixer script
# using OnTime SQL data made by DiaDemiEmi
# PLEASE READ README.md BEFORE USING

import re
import os
import mariadb
from nbt import nbt
from dotenv import load_dotenv

load_dotenv()
playerdata_location = os.getenv('PLAYERDATA_LOCATION')
db_user = os.getenv('DB_USER')
db_host = os.getenv('DB_HOST')
db_password = os.getenv('DB_PASSWORD')
db_database = os.getenv('DB_DATABASE')
db_table = os.getenv('DB_TABLE')

# Attempt to connect to the MariaDB server
try:
    conn = mariadb.connect(
        user=db_user,
        password=db_password,
        host=db_host,
        port=3306,
        database=db_database

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")

cur = conn.cursor()

# Execute query to get the uuid and firstlogin fields in the table
cur.execute(
    "SELECT uuid,firstlogin FROM `{0}` WHERE firstlogin IS NOT NULL".format(db_table),
)

# For every uuid and firstlogin in this table, attempt to
# open a file called uuid.dat and replace the firstPlayed tag 
# inside the bukkit compound with the new variable.
# Then write this to a file and repeat for every others.
for (uuid, firstlogin) in cur:
    print(uuid, firstlogin)
    file_path = "{0}/{1}.dat".format(playerdata_location, uuid)
    try:
        file = nbt.NBTFile(file_path, 'rb')
        print("Changing {0} to {1} for {2}".format(file["bukkit"]["firstPlayed"].value, firstlogin, uuid))
        file["bukkit"]["firstPlayed"].value = firstlogin
        file.write_file(file_path)
    except:
        print("UUID {0} has no playerdata file".format(uuid))

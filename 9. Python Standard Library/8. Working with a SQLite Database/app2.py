# Reading an SQLite Database
import sqlite3
import json
from pathlib import Path

with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)  # iterable object
   # for row in cursor:
    #    print(row)
    movies = cursor.fetchall()
    print(movies)

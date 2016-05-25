import sqlite3

conn = sqlite3.connect('music.sqlite3')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Tracks ')
# Removes Tracks table if it exists
# DROP TABLE command deletes the table and all 
# of its contents. Has no 'undo'
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')
# creates a table named Tracks with text column 
# named title and integer column named plays

conn.close()


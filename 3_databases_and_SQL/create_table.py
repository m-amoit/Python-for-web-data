import sqlite3

conn = sqlite3.connect('music.sqlite3')
cur = conn.cursor()

''' Insert rows into the table'''
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ? )',
	('Thunderstruck', 20 ))
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ? )',
	('My Way', 15))
conn.commit() #commit() writes data to database file

print 'Tracks:'

'''Retrieve rows from table'''
cur.execute('SELECT title, plays FROM Tracks')
for row in cur: #cursor() is iterable. Data read on demand as loop executes
	print row

#output: u' - unicode strings capable of storing non-Latin character sets

# cur.execute('DELETE FROM Tracks WHERE plays < 100')
# conn.commit()

cur.close()


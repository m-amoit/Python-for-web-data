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
# cur.execute('SELECT title, plays FROM Tracks')
''' * returns all columns for each row that matches the WHERE clause 
logical operators: =, <, >, <=, >=, !=, AND, OR'''
# cur.execute('SELECT * FROM Tracks WHERE title = "My Way"')

'''optional ORDER BY to control sorting of the returned rows'''
cur.execute('SELECT title, plays FROM Tracks ORDER BY plays')

for row in cur: #cursor() is iterable. Data read on demand as loop executes
	print row
#output: u' - unicode strings capable of storing non-Latin character sets

'''Update a column within 1+ rows in a table. Where specifies rows to be
updated. Else all rows will be updated.'''
cur.execute('UPDATE Tracks SET plays = 16 WHERE title = "My Way"')
conn.commit()

'''Remove rows, WHERE specifies which rows to delete'''
cur.execute('DELETE FROM Tracks WHERE plays < 100')
conn.commit()

cur.close()


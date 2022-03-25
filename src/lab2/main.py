import sqlite3

connect = sqlite3.connect('resources/example.db')

cursor = connect.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS stocks
               (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
cursor.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
connect.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
connect.close()

import sqlite3

db = 'products.sqlite'

with sqlite3.connect(db) as conn:
    conn.execute('CREATE TABLE IF NOT EXISTS products (product_id INTEGER PRIMARY KEY, name TEXT UNIQUE, quantity INT)')
conn.close()

name = 'jacket'
quantity = 5

try: 
    with sqlite3.connect(db) as conn:
        conn.execute('INSERT INTO products (name, quantity) VALUES (?, ?)', (name, quantity)) # if you creating own pk, you have to specify column names in INSERT statements
    conn.close()
except Exception as e:
    print('Error inserting ', e)

conn = sqlite3.connect(db)

results = conn.execute('SELECT * FROM products') # you have to specify (rowid) to see it in output if you are using the default pk of sqlite. like select rowid, * from....
for row in results:
    print(row)
conn.close()

print('end of program') # shows the program continues after handling error
import sqlite3

db = 'first_db.sqlite'

# conn = sqlite3.connect('first_db.sqlite') # creates the DB file if not exist and connects to it || connects to the DB if exists already

# context manager is good to use when we need to update or commit changes to db
# conn.commit() # changes finalized and saved in db - not needed with context manager
def create_table():
    with sqlite3.connect(db) as conn: # context manager takes care of commiting changes to the database and it is safer
        conn.execute('CREATE TABLE IF NOT EXISTS products (id int, name text)')
    
    conn.close()
    

def insert_example_data():
    with sqlite3.connect(db) as conn:
        conn.execute('INSERT INTO products values (1000, "hat")')
        conn.execute('INSERT INTO products values (1001, "jacket")')
    conn.close()
    

def display_all_data():
    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM products')
    print('All products: ')
    for row in results:
        print(row) # Each row is a tuple.
    conn.close()
    
def display_one_product(product_name):
    conn = sqlite3.connect(db)
    results =  conn.execute ('SELECT * FROM products WHERE name like ?', (product_name, ))
    first_row = results.fetchone()
    if first_row:
        print('Your product is : ',first_row) # upgrade to row factory later?
    else:
        print('not found')
    conn.close()
    

def create_new_product():
    new_id = int(input('enter new id: '))
    new_name = input('enter new product: ')
    with sqlite3.connect(db) as conn:
        conn.execute('INSERT INTO products VALUES (? , ? )', (new_id, new_name)) # paramaterized statements - safer from hacker or sqlite operational error
    # conn.commit() - with context takes care of committing changes to db
    conn.close()
    
def update_product():
    updated_product = 'phone'
    update_id = 1004
    with sqlite3.connect(db) as conn:
        conn.execute('UPDATE products SET name = ? WHERE id = ?', (updated_product, update_id))
    # conn.commit()
    conn.close()
    
def delete_product(product_name):
    with sqlite3.connect(db) as conn:
        conn.execute('DELETE FROM products WHERE name = ?', (product_name, )) # tuple - needs a comma at the end if its just one parameter
    # conn.commit()

    conn.close() # always close the DB at the end - needed even with context connection

create_table()

insert_example_data()

display_all_data()

display_one_product('jacket')

display_one_product('coat')

create_new_product()

update_product()

delete_product('jacket')

display_all_data()


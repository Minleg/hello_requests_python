"""
A menu - you need to add the database and fill in the functions. 
"""
import sqlite3

db = 'chainsawrecords.sqlite'

def main():
    create_table()
    menu_text = """
    1. Display all records
    2. Search by name
    3. Add new record
    4. Edit existing record
    5. Delete record 
    6. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            search_by_name()
        elif choice == '3':
            add_new_record()
        elif choice == '4':
            edit_existing_record()
        elif choice == '5':
            delete_record()
        elif choice == '6':
            break
        else:
            print('Not a valid selection, please try again')

def create_table():
    """ Create table in the database """
    with sqlite3.connect(db) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS chainsaw (name text, country text, catches int)')
    conn.close()


def display_all_records():
    conn = sqlite3.connect(db)
    records = conn.execute('SELECT * FROM chainsaw')
    for record in records:
        print(record)
    conn.close()
    #print('todo display all records')


def search_by_name():
    #print('todo ask user for a name, and print the matching record if found. What should the program do if the name is not found?')
    name = input('Enter the name to search: ')
    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM chainsaw WHERE name like ?', (name,))
    best_match = results.fetchone()
    if best_match:
        print('Search result: ', best_match)
    else:
        print('Not found. Please try again')
    conn.close()

def add_new_record():
    # print('todo add new record. What if user wants to add a record that already exists?')
    name = input('Enter name: ')
    country = input(f'Enter country for {name} : ')
    catches = int(input(f'Enter the number of catches for {name} : '))
    with sqlite3.connect(db) as conn:
        results = conn.execute('SELECT * FROM chainsaw where name like ? and country like ?', (name, country))
        result = results.fetchone()
        if result:
            print('It looks like our records already contains a record for the person.')
        else:
            conn.execute('INSERT INTO chainsaw VALUES (?,?,?)', (name,country,catches))
    conn.close()


def edit_existing_record():
    #print('todo edit existing record. What if user wants to edit record that does not exist?') 
    name = input('Enter name: ')
    country = input(f'Enter country for {name} : ')
    catches = int(input(f'Enter the number of catches for {name} : '))
    with sqlite3.connect(db) as conn:
        results = conn.execute('SELECT * FROM chainsaw where name like ? and country like ?', (name, country))
        result = results.fetchone()
        if result:
            conn.execute('UPDATE chainsaw SET catches = ? WHERE name = ? and country = ? ', (catches,name,country))
        else:
            print(f'No records for {name}. Select the option to add new record')
            # conn.execute('INSERT INTO chainsaw VALUES (?,?,?)', (name,country,catches))
    conn.close()
    
    


def delete_record():
    #print('todo delete existing record. What if user wants to delete record that does not exist?')
    name = input('Enter name: ')
    country = input(f'Enter country for {name} : ')
    with sqlite3.connect(db) as conn:
         results = conn.execute('SELECT * FROM chainsaw WHERE name like ? and country like ?', (name, country))
         result = results.fetchone()
         if result:
             conn.execute('DELETE FROM chainsaw WHERE name = ? and country = ?', (name, country))
    conn.close()            


if __name__ == '__main__':
    main()
"""
A menu - you need to add the database and fill in the functions. 
"""
from peewee import *

db = SqliteDatabase('chainsawPeewee.sqlite')

class Juggler(Model):
    name = CharField()
    country = CharField()
    counts = IntegerField()
    
    class Meta:
        database = db
    
    def __str__(self):
        return f'{self.name} {self.country} {self.counts}'


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
    db.connect()
    db.create_tables([Juggler])


def display_all_records():
    # print('todo display all records')
    records = Juggler.select()
    for record in records:
        print(record)


def search_by_name():
    # print('todo ask user for a name, and print the matching record if found. What should the program do if the name is not found?')
    search_name = input('Enter the name of the player: ')
    player = Juggler.get_or_none(name = search_name)
    if player:
        print(player)
    else:
        print(f'There is no player with name {search_name} in database')

def add_new_record():
    # print('todo add new record. What if user wants to add a record that already exists?')
    name = input('Enter name: ')
    country = input('Enter country: ')
    count = int(input('Enter number of catches: '))
    
    record_object = Juggler(name = name , country = country, counts = count)
    record_object.save()


def edit_existing_record():
    # print('todo edit existing record. What if user wants to edit record that does not exist?')
    player_name = input('Enter the name of the player to update: ')
    new_catch = int(input('Enter new catch: '))
    rows_modified = Juggler.update(counts=new_catch).where(Juggler.name == player_name).execute() 
    if rows_modified:
        print(f'Data is updated for player {player_name}')
    else:
        print(f'Record doesn\'t exist for {player_name}')


def delete_record():
    # print('todo delete existing record. What if user wants to delete record that does not exist?')
    player_name = input('Enter name: ')
    rows_deleted = Juggler.delete().where(Juggler.name == player_name).execute()
    if rows_deleted:
        print(f'Player {player_name} data has been deleted')
    else:
        print(f'Record for {player_name} does\'t exist') 


if __name__ == '__main__':
    main()
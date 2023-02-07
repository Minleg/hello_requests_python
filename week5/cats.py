from peewee import *

"""read documentation of peewee
   Peewee will set up the database for us. Peewee will create id field if pk not set up """

db = SqliteDatabase('cats.sqlite') # .sqlite, .db - can use any

class Owner(Model):
    name = CharField()
    
    class Meta:
        database = db
    
    def __str__(self):
        return f'{self.id}: {self.name}'

class Cat(Model):
    """ Cat class to model Cat table in database. Cat class have to be a subclass of Peewee Model class
        It allows us to specify the type of the variable like CharField, IntegerField etc """
    name = CharField()
    color = CharField()
    age = IntegerField()
    # owner = ForeignKeyField(Owner, backref='cats')
    
    class Meta:
        database = db
        
    def __str__(self):
        return f'{self.id}, {self.name}, {self.color}, {self.age}'

db.connect()
db.create_tables([Cat, Owner])

"""
sam = Owner(name='Sam')
sam.save()
lily = Cat(name='Lily', color = 'Black', age=1, owner=sam)
lily.save()
print(lily)
print(lily.owner.name)
"""

# Delete Operation
Cat.delete().execute() # clear the database table

# Create operation:  create Cat object, save it in db
zoe = Cat(name='Zoe', color='Ginger', age=3)
zoe.save() # make sure to save

holly = Cat(name='Holly', color='Tabby', age=5)
holly.save()

fluffy = Cat(name='Fluffy', color='Black', age=1)
fluffy.save()

# Read operation - Select * from cats
cats = Cat.select() # cats is a query object, you can't access each element here by index
for cat in cats:
    print(cat)

list_of_cats = list(cats) # now this is a regular Python list

""" CRUD operations
Create - insert
Read - select
Update
Delete
"""

# Update operation
fluffy.age = 2
fluffy.save()

# Update operation - 2nd version - may update many rows if needed.
rows_modified = Cat.update(age=6).where(Cat.name == 'Holly').execute()

print('After Fluffy and Holly age changed')
for cat in Cat.select():
    print(cat)

print(rows_modified)

buzz = Cat(name='Buzz', color='Gray', age=3)
buzz.save()

cats_who_are_3 =  Cat.select().where(Cat.age == 3)
for cat in cats_who_are_3:
    print(cat, ' is three')
    
cat_with_l_in_name = Cat.select().where(Cat.name % '*l*') # case sensitive, if we search b, Buzz won't be there in result
for cat in cat_with_l_in_name:
    print(cat, 'has l in name')

cat_with_b_in_name = Cat.select().where(Cat.name.contains('b')) # case insensitive - Buzz will be in result
for cat in cat_with_b_in_name:
    print(cat, 'has b in name')
    
zoe_from_db = Cat.get_or_none(name='Zoe') # returns one Cat object with name Zoe or it will return none if doesn't exist
print(zoe_from_db)

cat_1 = Cat.get_by_id(1) # will raise self.model.DoesNotExist exception if id doesn't exist in db, safer to use get_or_none() method
print(cat_1)

cat_100 = Cat.get_or_none(id = 100)
print(cat_100)

# Count, sort, limit
total = Cat.select().count()
print(total, 'cats in Database')

total_cats_who_are_3 = Cat.select().where(Cat.age == 3).count()
print('Number of cats who are 3 years old', total_cats_who_are_3)

# Sorting
cats_by_name = Cat.select().order_by(Cat.name)
print(list(cats_by_name))

cats_by_age = Cat.select().order_by(Cat.age)
print(list(cats_by_age))

# sorting in descending order of age
cats_by_age_desc = Cat.select().order_by(Cat.age.desc())  
print(list(cats_by_age_desc))

# sorting by descending order of age and then descending order of name
cats_by_age_desc_name_desc = Cat.select().order_by(Cat.age.desc(), Cat.name.desc()) # replace with just Cat.name and see the difference
print(list(cats_by_age_desc_name_desc))

print('First three cats in database:')
first_3 = Cat.select().limit(3)
for cat in first_3:
    print(cat)

print('First three cats in database ordered by name:')
first_3_order_by_name = Cat.select().order_by(Cat.name).limit(3)
for cat in first_3_order_by_name:
    print(cat)

# delete

rows_deleted = Cat.delete().where(Cat.name == 'Holly').execute()
print(rows_deleted, list(Cat.select()))

Cat.delete().execute() # deletes everything in db
print(list(Cat.select()))


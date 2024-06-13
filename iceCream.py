import sqlite3

# Connects to a Database
conn = sqlite3.connect('iceCreamParlour.db') 

#Creating a cursor
c = conn.cursor()

#Create a Table for Seasonal FLavours
c.execute(""" 
               CREATE TABLE IF NOT EXISTS seasonal_flavours (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   flavour_name TEXT
               )
               """)

#Create a Table for Ingredient Inventory
c.execute(""" 
               CREATE TABLE IF NOT EXISTS ingredient_inventory (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   ingredient TEXT,
                   quantity INT
               )
               """)

#Create a Table for Customer Suggestions
c.execute(""" 
               CREATE TABLE IF NOT EXISTS customer_suggestions (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   flavour_name TEXT,
                   suggested_by TEXT
               )
               """)

#Create a Table for Allergens
c.execute(""" 
               CREATE TABLE IF NOT EXISTS  allergens (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   allergen_name TEXT
               )
               """)

#Create a Table for Cart
c.execute(""" 
               CREATE TABLE IF NOT EXISTS cart (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   flavour_name TEXT
               )
               """)


# Inserting Values Into Seasonal Flavours Table (Already in Stock)
flavours = [
    ('Chocolate',),('Cookies and Cream',),('Strawberry',),('Mango',),('Black Current',)
]
c.executemany("Insert into seasonal_flavours ( flavour_name ) VALUES (?)" , flavours)


# Inserting Values Into Ingredients Table (Already in Stock)
ingredients = [
    ('Sugar',10 ,),('Choco Chips' , 9,),('Strawberries' , 12,),('Mango' ,15,),('Berries' , 20,)
]
c.executemany("Insert into ingredient_inventory ( ingredient , quantity ) VALUES (?,?)" , ingredients)

#Commit to the changes
conn.commit()

#Close the DB
conn.close()

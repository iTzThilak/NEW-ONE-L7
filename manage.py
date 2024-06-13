import sqlite3

class Manage : 
    #Constructor to initiate manager object which will let us access Databases
    def __init__ (self , db = "iceCreamParlour.db"):
        self.conn = sqlite3.connect(db)
        self.c = self.conn.cursor()
    
    # Lets the user add new flavours to the DB
    def add_seasonal_flavour(self, flavour_name):
        self.c.execute("INSERT INTO seasonal_flavours (flavour_name) VALUES (?)",
                       (flavour_name,))
        self.conn.commit()
    
    #Lets the user add the ingredients and their quantity in their inventory
    def add_ingredient(self, ingredient_name, quantity):
        self.c.execute("INSERT INTO ingredient_inventory (ingredient, quantity) VALUES (?, ?)",
                       (ingredient_name, quantity))
        self.conn.commit()
    
    # View customer suggested flavours  
    def view_customer_suggestions(self):
        self.c.execute("SELECT * FROM customer_suggestions")
        return self.c.fetchall()
    
    # View Allergens 
    def view_allergens(self):
        self.c.execute("SELECT * FROM allergens")
        return self.c.fetchall()
    
    #View the ingredients in the inventory
    def view_ingredients(self):
        self.c.execute("SELECT * FROM ingredient_inventory")
        return self.c.fetchall()

    # View all the flavours available
    def view_seasonal_flavours(self):
        self.c.execute("SELECT * FROM seasonal_flavours")
        return self.c.fetchall()
    
    #lets the Manager see what is in user's cart
    def view_cart(self):
        self.c.execute("SELECT * FROM cart")
        return self.c.fetchall()

    # Lets user to remove flavours
    def remove_flavour(self, flavour_name):
        self.c.execute("DELETE FROM seasonal_flavours WHERE flavour_name = ?",
                       (flavour_name,))
        self.conn.commit()

    #Lets user remove ingredients which have exhausted
    def remove_ingredient(self, ingredient):
        self.c.execute("DELETE FROM ingredient_inventory WHERE ingredient = ?",
                       (ingredient,))
        self.conn.commit()
    
    # Close DB
    def close(self):
        self.conn.close()


#initiating Object for manager to manage the parlor  
manage = Manage()

# Functions are defined to Call their corrosponding functions inside the class after taking user inputs
def add_seasonal_flavour():
    flavour_name = input("Enter flavour name: ")
    manage.add_seasonal_flavour(flavour_name)
    print("flavour added successfully!")

def add_ingredient():
    ingredient_name = input("Enter ingredient name: ")
    quantity = int(input("Enter quantity: "))
    manage.add_ingredient(ingredient_name, quantity)
    print("Ingredient added successfully!")

def view_customer_suggestions():
    suggestions = manage.view_customer_suggestions()
    print("Customer suggestions:")
    for row in suggestions:
        print(row)

def view_allergens():
    allergens = manage.view_allergens()
    print("Allergens:")
    for row in allergens:
        print(row)

def view_ingredients():
    ingredients = manage.view_ingredients()
    print("Ingredients:")
    for row in ingredients:
        print(row)

def view_seasonal_flavours():
    flavours = manage.view_seasonal_flavours()
    print("Seasonal flavours:")
    for row in flavours:
        print(row)

def view_cart():
    cart = manage.view_cart()
    print("Cart contents:")
    for row in cart:
        print(row)
        
def remove_flavour():
    flavour_name = input("Enter flavour name to remove: ")
    manage.remove_flavour(flavour_name)
    print("flavour removed successfully!")
    
def remove_ingredient():
    ingredient_name = input("Enter ingredient name to remove: ")
    manage.remove_ingredient(ingredient_name)
    print("Ingredient removed successfully!")

#This dictionary makes it easier for user to navigate through the options available
actions = {
    '1': add_seasonal_flavour,
    '2': add_ingredient,
    '3': view_customer_suggestions,
    '4': view_allergens,
    '5': view_ingredients,
    '6': view_seasonal_flavours,
    '7': view_cart,
    '8': remove_flavour,
    '9': remove_ingredient
}

#This application keeps running until we press 10 to exit
while True:
    print("\nIce Cream manage Menu:")
    print("1. Add Seasonal Flavor")
    print("2. Add Ingredient")
    print("3. View Customer Suggestions")
    print("4. View Allergens")
    print("5. View Ingredients")
    print("6. View Seasonal Flavors")
    print("7. View Cart")
    print("8. Remove Flavor")
    print("9. Remove Ingredient")
    print("10. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '10':
        #break condition
        print("Goodbye!")
        break
    elif choice in actions:
        # call functions from actions dictionary using the key given by user
        actions[choice]()
    else:
        print("Invalid choice. Please try again.")

manage.close()
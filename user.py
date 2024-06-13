import sqlite3

class IceCreamParlour : 
    #Constructor to initiate user object which will let us access Databases
    def __init__ (self , db = "iceCreamParlour.db"):
        self.conn = sqlite3.connect(db)
        self.c = self.conn.cursor()
    
    #To insert customer suggestions into customer_suggestions DB
    def add_customer_suggestion(self, flavour_name, suggested_by):
        self.c.execute("INSERT INTO customer_suggestions (flavour_name, suggested_by) VALUES (?, ?)",
                       (flavour_name, suggested_by))
        print ( flavour_name , " has been suggested. ")
        self.conn.commit()
    
    # To understand cstomers allergy concerns
    def add_allergen(self, allergen_name):
        self.c.execute("INSERT INTO allergens (allergen_name) VALUES (?)",
                       (allergen_name,))
        print ( allergen_name , " has been added. ")
        self.conn.commit()
        
    #Allows user to search for flavours
    def search_flavours(self, keyword):
        self.c.execute("SELECT * FROM seasonal_flavours WHERE flavour_name LIKE (?)",
                       ('%' + keyword + '%',))
        return self.c.fetchall()
    
    #adds ice creams to Cart
    def add_to_cart(self, flavour_name):
        self.c.execute("SELECT flavour_name FROM seasonal_flavours WHERE flavour_name = ?", (flavour_name,))
        if self.c.fetchone():
            self.c.execute("INSERT INTO cart (flavour_name) VALUES (?)", (flavour_name,))
            print(flavour_name, "has been added to cart.")
            self.conn.commit()
        else:
            print(flavour_name, "is not available in seasonal flavours. Please choose a different flavour.")
        
    #Allows user to see what they have put in cart
    def view_cart(self):
        self.c.execute("SELECT * FROM cart")
        print( "Cart items : ")
        return self.c.fetchall()
    
    #Allows user to remove flavours they dont want to buy
    def remove_from_cart(self, flavour_name):
        self.c.execute("DELETE FROM cart WHERE flavour_name = ?",
                       (flavour_name,))
        self.conn.commit()
    
    #Closing DB
    def close(self):
        self.conn.close()
        
#initiating Object
user = IceCreamParlour()


# Functions are defined to Call their corrosponding functions inside the class after taking user inputs
def add_customer_suggestion():
    flavour_name = input("Enter suggested flavour name: ")
    suggested_by = input("Enter your name: ")    
    user.add_customer_suggestion(flavour_name, suggested_by)

def add_allergen():
    allergen_name = input("Enter allergen name: ")
    user.add_allergen(allergen_name)
    print("Allergen added successfully!")
    
def search_flavours():
    print("Press Enter to see all Items available. ")
    keyword = input("Enter keyword to search: ")
    results = user.search_flavours(keyword)
    print("Search results:")
    for row in results:
        print(row)
        
def add_to_cart():
    flavour_name = input("Enter flavour name to add to cart: ")
    user.add_to_cart(flavour_name)
    
def view_cart():
    cart = user.view_cart()
    print("Cart contents:")
    for row in cart:
        print(row)

def remove_from_cart():
    flavour_name = input("Enter flavour name to remove from cart: ")
    user.remove_from_cart(flavour_name)
    print("flavour removed from cart successfully!")     
        
        
#This dictionary makes it easier for user to navigate through the options available
actions = {
        '1': add_customer_suggestion,
        '2': add_allergen,
        '3': search_flavours,
        '4': add_to_cart,
        '5': view_cart,
        '6': remove_from_cart,
    }

#This application keeps running until we press 7 to exit
while True:
        print("\nIce Cream Parlor Menu:")
        print("1. Add Customer Suggestion")
        print("2. Add Allergen")
        print("3. Search flavours")
        print("4. Add to Cart")
        print("5. View Cart")
        print("6. Remove from Cart")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '7':
            #break condition
            print("Goodbye!")
            break
        # call functions from actions dictionary using the key given by user
        elif choice in actions:
            actions[choice]()
        else:
            print("Invalid choice. Please try again.")





    
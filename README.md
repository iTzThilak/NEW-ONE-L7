# iceCreamParlour

# 📄 Documentation of the Code :
## Overview
This project is a simple database management system for an ice cream parlour. It uses SQLite to manage data about seasonal flavours, ingredients, customer suggestions, allergens, and a shopping cart. The system is divided into three main parts: database setup (iceCream.py), user interactions (user.py), and management operations (manage.py).

## Files
## iceCream.py
This script sets up the initial database structure and populates it with some initial data.

### Key Components:
Database Connection:

Establishes a connection to the SQLite database named iceCreamParlour.db.
Creates a cursor object for executing SQL commands.
### Table Creation:

Creates the following tables if they do not already exist:<br>
seasonal_flavours: Stores flavours available seasonally.<br>
ingredient_inventory: Stores ingredients and their quantities.<br>
customer_suggestions: Stores customer suggestions for new flavours.<br>
allergens: Stores allergens to be aware of.<br>
cart: Stores items added to the cart by the user.<br>
Initial Data Insertion:<br>

Populates the seasonal_flavours table with predefined flavours.<br>
Populates the ingredient_inventory table with predefined ingredients and their quantities.<br>
Commit and Close:<br>

Commits the changes to the database and closes the connection.<br>
## user.py
This script defines the IceCreamParlour class, which provides methods for users to interact with the database, such as adding customer suggestions, searching for flavours, adding items to the cart, and viewing or removing items from the cart.<br>

### Key Components:
Class IceCreamParlour:<br>

Constructor (__init__): Initializes the database connection and cursor.<br>
add_customer_suggestion: Inserts customer suggestions into the customer_suggestions table.<br>
add_allergen: Inserts allergens into the allergens table.<br>
search_flavours: Searches for flavours in the seasonal_flavours table based on a keyword.<br>
add_to_cart: Adds a flavour to the cart if it is available in the seasonal_flavours table.<br>
view_cart: Retrieves and prints all items in the cart.<br>
remove_from_cart: Removes a specified flavour from the cart.<br>
close: Closes the database connection.<br>
User Interaction Functions:<br>

Functions to handle user inputs and call the corresponding class methods.<br>
A dictionary (actions) maps user input to the appropriate function.<br>
A loop continuously displays the menu and processes user input until the user chooses to exit.<br>
## manage.py
This script defines the Manage class, which provides methods for managers to interact with the database, such as adding new seasonal flavours, managing ingredients, viewing customer suggestions and allergens, and viewing or removing items from the inventory.<br>

### Key Components:
Class Manage:

Constructor (__init__): Initializes the database connection and cursor.<br>
add_seasonal_flavour: Adds a new flavour to the seasonal_flavours table.<br>
add_ingredient: Adds a new ingredient and its quantity to the ingredient_inventory table.<br>
view_customer_suggestions: Retrieves and prints all customer suggestions.<br>
view_allergens: Retrieves and prints all allergens.<br>
view_ingredients: Retrieves and prints all ingredients in the inventory.<br>
view_seasonal_flavours: Retrieves and prints all seasonal flavours.<br>
view_cart: Retrieves and prints all items in the cart.<br>
remove_flavour: Removes a specified flavour from the seasonal_flavours table.<br>
remove_ingredient: Removes a specified ingredient from the ingredient_inventory table.<br>
close: Closes the database connection.<br>
Manager Interaction Functions:<br>

Functions to handle manager inputs and call the corresponding class methods.<br>
A dictionary (actions) maps manager input to the appropriate function.<br>
A loop continuously displays the menu and processes manager input until the manager chooses to exit.<br>
## Usage
### Database Setup:

Run iceCream.py to set up the database and populate it with initial data.
### User Interaction:

Run user.py to allow users to interact with the system. They can suggest new flavours, add items to their cart, view the cart, and more.
### Manager Interaction:

Run manage.py to allow managers to manage the parlour. They can add new flavours and ingredients, view customer suggestions and allergens, and manage the inventory.
Each script provides a menu-driven interface to facilitate interactions, making it easy for users and managers to navigate through the available options.


# 🚀 How to use ?

1. Clone the Repository to your system.
2. ```sh
    git clone https://github.com/SantoshIyer30/iceCreamParlour.git
    cd iceCreamParlor
    ```
3. Open "iceCream.py" and execute the file. This step will create necessary databases for further operations.
4. ```sh
    python iceCream.py
    ```
5. Open "user.py" to access the Parlor like a customer.
6. ```sh
    python user.py
    ```
7. When executed , the application has a text based menu where you get to choose actions from the given options as a user. i.e add and remove items from cart, view offerings, add allergens, suggest new flavours.
8. Open "manage.py" to access the Parlor as a manager.
9. ```sh
    python manage.py
    ```
10. When executed, the manager also has a text based menu which gives the user to choose which action to execute from the given options. i.e view user cart, view inventory, add/ remove items from inventory, view user suggestions , and many more.


## Docker 
1. Build the Docker Image from the docker file<br>
```sh 
    Docker build -t icecreamparlor .
```
2. To Create the container<br>
   ```sh
   Docker run -h -it icecreamparlor
   ```
3. To ge docker container info from which we will copy Conainer ID<br>
   ```sh
   Docker Container ls
   ```
4. To open terminal in docker<br>
   ```sh
   Docker exec [Container ID] bash
    ```
5. Now , to initiate the program, first we run iceCream.py<br>
   ```sh
   python iceCream.py
   ```
6. To open user.py<br>
   ```sh
   python user.py
   ```
7. To open manage.py<br>
   ```sh
   python mange.py
   ```
   <br>
# 💻 Test Steps 

### In user.py 
We observe a menu which looks like : <br>
***Ice Cream Parlor Menu:***
1. ***Add Customer Suggestion***
2. ***Add Allergen***
3. ***Search flavours***
4. ***Add to Cart***
5. ***View Cart***
6. ***Remove from Cart***
7. ***Exit***
***Enter your choice :***
<br>
1. Enter the desired choice, For example we press 1 and press enter<br>
2. We are asked to enter our suggested flavour and our name <br>

***Enter your choice: 1*** <br>
***Enter suggested flavour name: Blue Berry*** <br>
***Enter your name: Santosh*** <br>
***Blue Berry  has been suggested.*** <br>

3. We can also perform other tasks like adding ice cream to cart, which can be done by pressing 4 and pressing enter <br>
***Enter your choice: 4*** <br>
***Enter flavour name to add to cart: Chocolate*** <br>
***Chocolate has been added to cart.*** <br>

4. We can Confirm the addition by pressing 5 and pressing enter <br>
***Enter your choice: 5*** <br>
***Cart contents:*** <br>
***(1, 'Chocolate')*** <br>

### In manage.py
The Interface is the same but they have different options. 
The options being :<br>
***Ice Cream manage Menu:***
1. ***Add Seasonal Flavor***
2. ***Add Ingredient***
3. ***View Customer Suggestions***
4. ***View Allergens***
5. ***View Ingredients***
6. ***View Seasonal Flavors***
7. ***View Cart***
8. ***Remove Flavor***
9. ***Remove Ingredient***
10. ***Exit***
***Enter your choice:***<br>

For example, let's confirm if our Blue Berry flavour has been added yet or not
1. Press 3 and Press enter <br>
***Enter your choice: 3***<br>
***Customer suggestions:***<br>
***(1, 'Blue Berry', 'Santosh')***


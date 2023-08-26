# this py file will mimick the application interface as I test out all classes and functionalities

from user import User
from product import Products
from cart import Cart
import json, random


# will be integrating the search.py functionality to pass products to app.py
products = Products.load_products_from_file('./output.json')

#Create a new user then login
User.register("mshallom", "micahshallom@gmail.com", "password123")

try:
    success, user_instance = User.login("mshallom", "password123")
    if success:
        print("Login successful.")
        # Perform actions with the user_instance
    else:
        print("Login failed.")
except Exception as e:
    print("An error occurred during login:", e)


if user_instance:
    user_cart = Cart(user_instance)

    #lets select some of the products which will go to the cart class
    #in real life this will be the user clicking the add-to-cart button on each desired product
    for i in range(5):
        user_cart.add_to_cart(products[i])

    #testing the removal of a product from cart
    if products == []:
        print("Cart is already empty. Nothing to remove")
    else:
        user_cart.remove_from_cart(products[1])

    #testing the order class functionality
    print(user_cart.checkout().get_order_details())

# if __name__ == "__main__":
#     print(main())
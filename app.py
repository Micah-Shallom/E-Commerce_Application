# this py file will mimick the application interface as I test out all classes and functionalities

from user import User
from product import Products
from cart import Cart
import json, random


# will be integrating the search.py functionality to pass products to app.py
products = Products.load_products_from_file('./output.json')

#Create a new user then login
User.register("mshallom", "micahshallom@gmail.com", "password123")
user = User.login("mshallom","password123")

if user[0]:
    print(products[1].price)
    user = user[1]
    user_cart = Cart(user)

    #lets select some of the products which will go to the cart class
    #in real life this will be the user clicking the add-to-cart button on each desired product
    for i in range(5):
        user_cart.add_to_cart(products[i])

    #testing the removal of a product from cart
    user_cart.remove_from_cart(products[1])
    print(len(user_cart.display_cart()))
    print(user_cart.calculate_total())

    #testing the order class functionality
    print(user_cart.checkout().get_order_details())

# if __name__ == "__main__":
#     print(main())
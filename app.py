# this py file will mimick the application interface as I test out all classes and functionalities

from user import User
from product import Products
from cart import Cart
from search import ProductSearch
import json, random

api_endpoint = "https://ecommerce-product-api1.p.rapidapi.com/data"

user_query = input("Enter a product name to search: ")

querystring = {
    "product": user_query,
    "page": "1"
}



# will be integrating the search.py functionality to pass products to app.py
# products = Products.load_products_from_file('./output.json')

products = ProductSearch(api_endpoint).search_products(querystring)

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
    for i in range(len(products)):
        user_cart.add_to_cart(products[i])

    cart = user_cart.display_cart()
    if cart:
        for product in cart:
            # print(product.__dict__.keys())
            print(f"Title: {product.title} \nPrice: {product.price}")
    else:
        print("No products found for the given query.")

    #testing the removal of a product from cart
    if products == []:
        print("Cart is already empty. Nothing to remove")
    else:
        user_cart.remove_from_cart(products[1])

    #testing the order class functionality
    # print(user_cart.checkout().get_order_details())



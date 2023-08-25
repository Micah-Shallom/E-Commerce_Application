from user import User
from product import Products
from cart import Cart
import json, random

def main():
    products = []
    with open("./output.json", 'r') as f:
        json_data = json.load(f)
    for item in json_data:
        product = Products(
            image=item.get('image'),
            title=item.get('title'),
            price=int(item.get('price')[3:].replace(',','')),
            description=item.get('description')
        )
        products.append(product)
    return products

#Create a new user then login
User.register("mshallom", "micahshallom@gmail.com", "password123")
user = User.login("mshallom","password123")

if user[0]:
    displayed_products = main() #Lets call the main function
    print(displayed_products[1].price)
    user_id = user[1].user_id
    user_cart = Cart(user_id)

    #lets select some of the products which will go to the cart class
    for i in range(5):
        user_cart.add_to_cart(displayed_products[i])

    #testing the removal of a product from cart
    user_cart.remove_from_cart(displayed_products[1])
    print(len(user_cart.display_cart()))
    print(user_cart.calculate_total())

# if __name__ == "__main__":
#     print(main())
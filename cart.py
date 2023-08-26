from order import Order
import datetime, uuid


class Cart:
    def __init__(self, user):
        self.user = user
        self.products = []
        self.total_price = 0
    
    def add_to_cart(self, product):
        self.products.append(product)
        self.total_price += product.price
    
    def remove_from_cart(self, product):
        self.products.remove(product)
        self.total_price -= product.price
    
    def display_cart(self):
        return self.products
    
    def calculate_total(self):
        return self.total_price
    
    def checkout(self):
        #generate order datetime
        current_datetime = datetime.datetime.now()
        order_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

        #generate order_id
        order_id = uuid.uuid4().hex[:10].upper()

        #instantiate order class for user product in cart
        order = Order(order_id, self.user_id,self.products,self.total_price,order_datetime)
        
        return order

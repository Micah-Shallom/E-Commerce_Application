class Cart:
    def __init__(self, user_id):
        self.user_id = user_id
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
        # Checkout logic
        pass

class Order:
    current_valid_coupons = {'group5dynamite':10,
                            'group5fortheWin':30}

    def __init__(self, order_id, user_id, products, order_total, order_date):
        self.order_id = order_id
        self.user_id = user_id
        self.products = products
        self.total_cost = order_total
        self.order_date = order_date
    
    def get_order_details(self):
        return f"Order_ID:{self.order_id}\nOrder_total:{self.order_total}\nOrder_datetime:{self.order_date}\nProducts_Ordered{self.products}"
    
    # def add_item(self, product, quantity, price):
    #     self.items.append({"product": product, "quantity": quantity, "price": price})
    #     self.total_cost += quantity * price

    def apply_coupon(self, coupon_code):
        if self.total_cost <= 0:
            print("No items in the order to apply the coupon to.")
            return
        if coupon_code not in Order.current_valid_coupons:
            return "Invalid Coupon Code"
        else:
            discount_percentage = Order.current_valid_coupons[coupon_code]
            discount_amount = (discount_percentage / 100) * self.total_cost
            self.total_cost -= discount_amount
            print(f"Coupon '{coupon_code}' applied. Discount of ${discount_amount:.2f} applied to the order.")

    def calculate_total_cost(self):
        return self.total_cost
    

    


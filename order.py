class Order:
    current_valid_coupons = {'group5dynamite':10,
                            'group5fortheWin':30}

    def __init__(self, order_id, user, products, order_total, order_date):
        self.order_id = order_id
        self.user = user
        self.products = products
        self.total_cost = order_total
        self.order_date = order_date
        self.status = "Pending"
    
    def get_order_details(self):
        return f"Order_ID:{self.order_id}\nOrder_total:{self.total_cost}\nOrder_datetime:{self.order_date}\nProducts_Ordered{self.products}"
    
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

    def place_order(self):
        if self.status != "Pending":
            return "Order has already been placed or processed."

        # Simulate payment processing
        payment_status = self.process_payment()

        if payment_status == "Success":
            # Simulate updating inventory
            inventory_updated = self.update_inventory()

            if inventory_updated:
                self.status = "Processing"
                return "Order placed successfully. Order is being processed."
            else:
                return "Failed to update inventory. Order could not be placed."
        else:
            return "Payment failed. Order could not be placed."

    def process_payment(self):
        # Return "Success" if payment is successful, otherwise return "Failed"
        return "Success"
    
    def update_inventory(self):
        return True
    

    


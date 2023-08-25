import uuid

def generate_order_id():
    order_id = uuid.uuid4().hex[:10].upper()
    return order_id

# Example usage
order_id = generate_order_id()
print("Generated Order ID:", order_id)



# import datetime
# current_datetime = datetime.datetime.now()
# formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
# print("Formatted Date and Time:", formatted_datetime)


# a = "10,999"

# print(type(int(a.replace(',',''))))
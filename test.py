# import uuid

# def generate_order_id():
#     order_id = uuid.uuid4().hex[:10].upper()
#     return order_id

# # Example usage
# order_id = generate_order_id()
# print("Generated Order ID:", order_id)



# # import datetime
# # current_datetime = datetime.datetime.now()
# # formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
# # print("Formatted Date and Time:", formatted_datetime)

# replacements = {
#     "₹":"",
#     ",":""
# }
# a = "₹10,999"
# for each in replacements.keys():
#     a = a.replace(each,replacements[each])

# print(a)


items = [
    {
        "title": "i am a title",
        "name": "shallom"
    },
    {
        "name": "shallom"
    },
    {
        "title": "i am a title",
        "name": "shallom"
    },
    {
        "title": "me",
        "sex": "shallom"
    }
]

for each in items:
    if "title" and "name" in each:
        print(each)
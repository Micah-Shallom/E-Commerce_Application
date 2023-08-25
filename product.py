import json

class Products:
    def __init__(self, image, title, price, description):
        self.image = image
        self.title = title
        self.price = price
        self.description = description

    # @classmethod
    # def instantiate_from_json(cls):
    #     products = []
    #     with open("./output.json", 'r') as f:
    #         json_data = json.load(f)
    #     for item in json_data:
    #         product = cls(
    #             image=item.get('image'),
    #             title=item.get('title'),
    #             price=item.get('price'),
    #             description=item.get('description')
    #         )
    #         products.append(product)
    #     return products
    
    def get_details(self):
        return f"ID: {self.image}, Title: {self.title}, Price: {self.price}"


from product import Product
import json

def main():
    products = []
    with open("./output.json", 'r') as f:
        json_data = json.load(f)
    for item in json_data:
        product = Product(
            image=item.get('image'),
            title=item.get('title'),
            price=item.get('price'),
            description=item.get('description')
        )
        products.append(product)
    return products

if __name__ == "__main__":
    print(main())
    # product_list  = Product.instantiate_from_json()
    # for each in product_list:
    #     print(each.get_details())
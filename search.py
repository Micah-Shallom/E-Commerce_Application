import requests
from product import Products


class ProductSearch:
	def __init__(self, api_endpoint):
		self.api_endpoint = api_endpoint

	def search_products(self, query):
		headers = {
			"X-RapidAPI-Key": "463ef49b89msh3cf45c255bf0477p19d199jsnc90357348d2f",
			"X-RapidAPI-Host": "ecommerce-product-api1.p.rapidapi.com"
		}
		response = requests.get(self.api_endpoint, headers=headers, params=query)
		if response.status_code == 200:
			# Parse the API response and create product instances
			api_data = response.json()
			products = []
			for item in api_data:
				if item["title"]: #because some of the items had no titles
						product = Products(
							image=item.get('image'),
							title=item.get('title'),
							price=int(item.get('price').replace('₹', '')),
							description=item.get('description')
						)
						products.append(product)
			return products
		else:
			print("Error fetching product data from the API.")
			return []

# if __name__ == "__main__":
# 	api_endpoint = "https://ecommerce-product-api1.p.rapidapi.com/data" 
	
# 	product_search = ProductSearch(api_endpoint)
	
# 	user_query = input("Enter a product name to search: ")
	
# 	querystring = {
# 		"product":user_query,
# 		"page":"1"
# 	}
	
# 	search_results = product_search.search_products(querystring)
	
# 	if search_results:
# 		for product in search_results:
# 			print(product.title, product.price)
# 	else:
# 		print("No products found for the given query.")



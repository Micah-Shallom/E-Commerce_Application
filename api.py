import requests

url = "https://ecommerce-product-api1.p.rapidapi.com/data"

querystring = {"product":"phone","page":"1"}

headers = {
	"X-RapidAPI-Key": "463ef49b89msh3cf45c255bf0477p19d199jsnc90357348d2f",
	"X-RapidAPI-Host": "ecommerce-product-api1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
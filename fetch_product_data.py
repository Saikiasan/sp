import requests

def fetch_product_data():
    url = "https://atomykeson.online/data/products/p.json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_product_data_for_gdp(gdp_value, product_data):
    for product in product_data:
        if product.get('gdp') == gdp_value:
            return product
    return None

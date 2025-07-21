
import requests
import pandas as pd
import time

def get_products(lat, lng, category_id):
    url = f"https://api.blinkit.com/v1/categories/{category_id}/products"
    params = {
        'lat': lat,
        'lng': lng
    }

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get("products", [])
    else:
        print(f"Failed for category {category_id} at {lat}, {lng}. Status code:", response.status_code)
        return []

def parse_product(product):
    return {
        "product_id": product.get("id"),
        "name": product.get("name"),
        "brand": product.get("brand"),
        "mrp": product.get("mrp"),
        "selling_price": product.get("price"),
        "discount": product.get("discount"),
        "quantity": product.get("quantity"),
        "image_url": product.get("image_url"),
        "rating": product.get("rating"),
    }

def main():
    input_df = pd.read_csv("categories_input.csv")
    output_data = []

    for _, row in input_df.iterrows():
        lat = row["latitude"]
        lng = row["longitude"]
        cat_id = row["category_id"]
        products = get_products(lat, lng, cat_id)

        for product in products:
            parsed = parse_product(product)
            parsed["latitude"] = lat
            parsed["longitude"] = lng
            parsed["category_id"] = cat_id
            output_data.append(parsed)
        
        time.sleep(1)  # Be respectful with delay between requests

    df = pd.DataFrame(output_data)
    df.to_csv("scraped_output.csv", index=False)
    print("Scraping completed. Data saved to scraped_output.csv.")

if __name__ == "__main__":
    main()

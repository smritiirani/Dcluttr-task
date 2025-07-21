# Dcluttr-task

# 🛒 BlinkIt Subcategory Scraper

This project scrapes product data from BlinkIt based on category IDs and geolocation (latitude, longitude). It uses BlinkIt's public API (used on subcategory pages) and saves the output into a structured CSV format.

## ✅ Features

- Uses public API to get live product listings from BlinkIt.
- Scrapes products for multiple categories and locations.
- Outputs CSV file with detailed product information.

## 🛠 Requirements

- Python 3.x
- Libraries:
  - `requests`
  - `pandas`

Install dependencies using:

```bash
pip install -r requirements.txt
📂 Files
blinkit_scraper.py - Python script to scrape data.
categories_input.csv - Input file with latitude, longitude, and category IDs.
scraped_output.csv - Output file generated after scraping.
blinkit_scraper_colab.ipynb - Google Colab version of the scraper.

README.md - Documentation.

📥 Input Format (categories_input.csv)
csv
Copy
Edit
latitude,longitude,category_id
28.6139,77.2090,355
19.0760,72.8777,456
📤 Output Columns
product_id
name
brand
mrp
selling_price
discount
quantity
image_url
rating
latitude
longitude
category_id

🚀 Usage
Option 1: Run Locally
bash
Copy
Edit
python blinkit_scraper.py
Option 2: Run on Google Colab
Open blinkit_scraper_colab.ipynb on Google Colab.

Upload categories_input.csv when prompted.

Run all cells.

CSV will be auto-downloaded.

Disclaimer: This project is for educational and research purposes only. It does not intend to violate BlinkIt's Terms of Service.

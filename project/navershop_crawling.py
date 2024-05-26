from bs4 import BeautifulSoup
import requests
from mongodb_connection import insert_db, get_db

keyword = "아이폰"
url = f"https://www.gmarket.co.kr/n/search?keyword={keyword}"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
product_list = soup.select("div.box__information-major")

item_list = []

for product in product_list:
  product_name = product.select_one("div.box__item-title").get_text().strip()
  product_price = product.select_one("div.box__item-price").select_one("strong.text__value").get_text().strip().replace(",", "").replace("원", "").replace("판매가", "")
  item_list.append({"product_name": product_name, "price": int(product_price)})

insert_db(item_list)

get_db([])


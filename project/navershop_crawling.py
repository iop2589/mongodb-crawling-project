from bs4 import BeautifulSoup
import requests
from mongodb_connection import insert_db, get_db

keyword = "아이폰"
item_list = []

for page_num in range(1, 11):
  url = f"https://www.gmarket.co.kr/n/search?keyword={keyword}&k=42&p={page_num}"
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")
  product_list = soup.select("div.box__information-major")


  for product in product_list:
    product_name = product.select_one("div.box__item-title").get_text().strip()
    product_price = product.select_one("div.box__item-price").select_one("strong.text__value").get_text().strip().replace(",", "").replace("원", "").replace("판매가", "")
    item_list.append({"product_name": product_name, "price": int(product_price)})
    
    
  print(item_list)

  insert_db(item_list)

  get_db([])


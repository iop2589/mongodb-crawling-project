import requests
from bs4 import BeautifulSoup
from mongo_db import insert_db, get_db

item_list = []
for page_num in range(10):
  if page_num == 0:
      url = "https://davelee-fun.github.io/"
  else:
    url = f"https://davelee-fun.github.io/page{page_num + 1}"
    
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")
  data = soup.select("div.card-body")
  
  for item in data:
    category = item.select_one("h2.card-title").get_text().replace("관련 상품 추천", "").strip()
    product = item.select_one("h4.card-text").get_text().replace("상품명:", "").strip()
    item_list.append({"category": category, "product": product})
    
insert_db(item_list)

get_db([])

pipe_line = [
  {
    "$group": {
      "_id": "$category",
      "count": { "$sum": 1 }
    }
  }
]

get_db(pipe_line)





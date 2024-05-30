import requests
import xmltodict
import json

url = "http://apis.data.go.kr/1613000/AptListService2/getTotalAptList"
detail_url = "http://apis.data.go.kr/1613000/AptBasisInfoService1/getAphusBassInfo"
service_key = "RyvpO+Rt0PTChV+b4ihzA/9pIhxUAC70BBjjG0UOBwrSOOXjtuM6X4zE60SJLwQMZNenqmuHiqCLkz6lbt6NLg=="
params = {"serviceKey": service_key, "pageNo": 1, "numOfRows": "10"}
response = requests.get(url, params=params)

result_json_detail_list = []

if response.status_code == 200:
  xmlData = response.text
  jsonStr = json.dumps(xmltodict.parse(xmlData), indent=4, ensure_ascii=False)
  result_object = None
  json_list = []
  result_object = json.loads(jsonStr)
  json_list.append(result_object["response"]["body"]["items"]["item"])
  print(json_list)
else:
  print("List 정보 조회 불가", response.status_code)
  
for json_data in json_list[0]:
  detail_params = {"serviceKey": service_key, "kaptCode": json_data["kaptCode"]}
  detail_reponse = requests.get(detail_url, params=detail_params)
  
  if detail_reponse.status_code == 200:
    detail_result = json.dumps(xmltodict.parse(detail_reponse.text), indent=4, ensure_ascii=False)
    detail_result_json = json.loads(detail_result)
    detail_info = detail_result_json["response"]["body"]["item"]
    print ("공동주택코드:", json_data["kaptCode"], 
          "공동주택명:", json_data["kaptName"], 
          "법정동코드:", detail_info["bjdCode"], 
          "아파트유형:", detail_info["codeAptNm"], 
          "관리방식:", detail_info["codeMgrNm"], 
          "주소:", detail_info["kaptAddr"], 
          "시공사:", detail_info["kaptBcompany"], 
          "시행사:", detail_info["kaptAcompany"])
  else:
    print("detail 정보 조회 불가", detail_reponse.status_code)
    


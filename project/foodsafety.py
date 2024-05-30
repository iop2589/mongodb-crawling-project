import requests
import json

api_codes = ["I1250", "I1310", "I2711"]

srch_param = "비타500"
result_list = []

for api_code in api_codes:
  url = f"http://openapi.foodsafetykorea.go.kr/api/f359a2a9db6642839f0c/{api_code}/json/1/10/DESC_KOR={srch_param}"
  response = requests.get(url)
  result_object = json.loads(response.text);
  if (response.status_code == 200 and result_object[api_code]["RESULT"]["CODE"] == "INFO-000"):
    json_array = result_object[api_code]["row"]
  else:
    print("조회 error", response.status_code)
    
  for json_result in json_array:
    result_list.append(json_result)
      

for result in result_list:
  print(
        "품목제조번호:", result["PRDLST_REPORT_NO"], "\n",
        "허가일자:", result["PRMS_DT"], "\n",
        "최종수정일자:", result["LAST_UPDT_DTM"], "\n",
        "인허가번호:", result["LCNS_NO"], "\n",
        "품목명:", result["PRDLST_NM"], "\n",
        "소비기한:", result["POG_DAYCNT"], "\n",
        "업소명", result["BSSH_NM"], "\n"
      )

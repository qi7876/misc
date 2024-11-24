import requests
import re

session = requests.Session()
url = "http://prob00-004.recruit.yulinsec.cn"

get_response = session.get(url, verify=False)

print("GET Status Code:", get_response.status_code)
print("GET Response Headers:", get_response.headers)
print("GET Response Body:\n", get_response.text)

expression_pattern = re.compile(r"(\d+\s*[\+\-\*/]\s*\d+)")
match = expression_pattern.search(get_response.text)

expression = match.group(1)
print(f"\nExtracted Expression: {expression}")

clean_expression = expression.replace(" ", "")
result = eval(clean_expression)
print(f"Calculated Result: {result}")
post_data = {"result": str(result)}

post_response = session.post(url, data=post_data)
post_response.raise_for_status()
print("POST Status Code:", post_response.status_code)
print("POST Response Headers:", post_response.headers)
print("POST Response Body:\n", post_response.text)

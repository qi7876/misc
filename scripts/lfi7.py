import requests

session = requests.Session()

params = {
    "a": "hacker",
}
response = session.get(
    "https://prob00-fcf77b3fdbf29ec6ec6f0c3dd5ad4ce5.recruit.yulinsec.cn/",
    params=params,
    verify=False,
)

cookies = response.cookies

# Iterate through cookies and print them
for cookie in cookies:
    print(f"{cookie.name}: {cookie.value}")

import requests

payload = {"name": "User"}
response = requests.get("https://playground.learnqa.ru/api/get_text", params=payload)
parsed_response_text = response.json()
print(parsed_response_text["answer"])

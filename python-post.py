import requests
api_url = "https://jsonplaceholder.typicode.com/todos"

todo = {"userId": 2, "title": "Buy milk", "completed": True}

response = requests.post(api_url, json=todo)

print(response.json())
print(response.status_code)

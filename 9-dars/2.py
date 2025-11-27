import requests

url = "https://jsonplaceholder.typicode.com/todos"
response = requests.get(url)
data=response.json()

print([e['userId'] for e in data])

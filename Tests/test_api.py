# import requests

# name = "John Smith"
# age = 39
# order = "Violence"

# url = f"https://api-customer-038j.onrender.com/customer?name={name}&age={age}&order={order}"

# response = requests.get(url)
# content = response.json()

# print(content)

import requests

url = "https://api-customer-038j.onrender.com/customer/"

data = {
    "name": "Rico",
    "age": 3,
    "order": "Stars"
}

response = requests.put(url, json=data)
content = response.json()

print(content)












# import requests

# url = "https://api-customer-038j.onrender.com/customer"

# data = {
#     "name": "John Smith",
#     "age": 39,
#     "order": "ABC123"
# }

# response = requests.post(url, json=data)
# content = response.json()

# print(content)


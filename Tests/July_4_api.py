# import requests

# response = requests.get(["https://api.publicapis.org/entries"])

# # print(response.content)
# print(response.status_code)


#acessing data from a dictionary on postman.co

import requests

response = requests.get("https://api.publicapis.org/entries")

content = response.json()

data = content["entries"][1]["API"]

print(data)





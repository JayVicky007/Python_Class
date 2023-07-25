# from bs4 import BeautifulSoup as BS
# import requests

# url = "https://goku.sx/"

# goku_sx = requests.get(url + "/home")

# container = goku_sx.find("div", class_ = "section-items section-items-default")
# items = container.find("")


import requests

file_url = "https://goku.sx/watch-movie/watch-mission-impossible-7-68135/1356223"
save_path = "c:\\Users\\Jay Vicky\\Videos\\Movies\\Mission_Impossible_Dead_Reckoning_Part_One"

response = requests.get(file_url)
response.raise_for_status()  # Check if the request was successful

with open(save_path, "wb") as file:
    file.write(response.content)

print("File downloaded successfully!")


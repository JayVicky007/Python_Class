from bs4 import BeautifulSoup
import requests


url = "https://goku.sx/home/"

response = requests.get(url)

content = BeautifulSoup(response.text, "html.parser")

container = content.find("div", class_ = "section-items section-items-default")

items = container.find_all("div", class_ = "item")
# images = container.find_all("div", class_ = "movie-thumbnail")
for item in items:
    print(item.text.strip())
    with open("Goku.txt", "a") as file:
        file.write(f"{item.text.strip()}")

# for image in images:
#     print(image["data-src"])

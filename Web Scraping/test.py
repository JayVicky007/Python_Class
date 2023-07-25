# from bs4 import BeautifulSoup
# import requests

# url = ("https://www.jumia.com.ng/sporting-goods/")

# response = requests.get(url)

# contents = BeautifulSoup(response.text, "html.parser") # convert the response to text. tells beautiful soup that we're passing html code

# container = contents.find("div", class_ = "crs row _no-g -fw-nw _6cl-4cm -pvxs")

# items = container.find_all("div", class_ ="itm col")


# for item in items:
#     image = item.find("img", class_ = "img")
#     print(image["data-src"])
#     name = item.find("div", class_ = "name")
#     print(name.text)
#     price = item.find("div", class_ = "prc")
#     print(price.text)


from bs4 import BeautifulSoup
import requests

url = ("https://www.jumia.com.ng/sporting-goods/")

response = requests.get(url)

contents = BeautifulSoup(response.text, "html.parser") # convert the response to text. tells beautiful soup that we're passing html code

container = contents.find("div", class_ = "row _no-g -tac -pvxs -phs _6c-shs")

items = container.find_all("div", class_ ="ar _3-4")

for item in items:
    # name = item.find("div", class_ = "name")
    # print(name.text)
    # price = item.find("div", class_ = "prc")
    # print(price.text)
    image = item.find("img", class_ = "-rad4")
    print(image["data-src"])





    




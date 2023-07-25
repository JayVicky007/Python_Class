from bs4 import BeautifulSoup
import requests

url = "https://goku.sx/"
response = requests.get(url + "/home")

content = BeautifulSoup(response.text, "html.parser")

container = content.find("div", class_ = "section-items section-items-default")
trending_movies = content.find_all("div", class_ = "item")

movies = {}
for movies in trending_movies:
    movie_info = movies.find("div", class_ = "movie-info")
    info_split = movie_info.find("div", class_ = "info-split")
    div = info_split.find_all("div")
    movie_link = movie_info.find("a", class_ = "movie-link")

    print()
    print(movie_link.text.strip())
    print(div[0].text)
    print(div[2].text)
    print(url + movie_link["href"])
    print()
    



import requests
from bs4 import BeautifulSoup

website = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(website)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
movie_titles = [tag.getText() for tag in soup.find_all("h3", class_="title")]
movie_titles.reverse()

with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")

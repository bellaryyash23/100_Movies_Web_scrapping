from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features"
                            "/best-movies-2/")
movies_100_web = response.text

soup = BeautifulSoup(movies_100_web, "html.parser")

movies_titles = [title.get_text() for title in soup.find_all(name="h3", class_="title")]

with open("movies_1.txt", mode="a", encoding="utf-8")as file:
    for i in range(len(movies_titles)-1, -1, -1):
        file.write(f"{movies_titles[i]} \n")


# movie_names = []
# for title in movies_titles:
#     try:
#         movie_names.append(title.split(") ")[1])
#     except IndexError:
#         movie_names.append(title.split(": ")[1])
#
# movie_no = 100
# with open("movies.txt", mode="a", encoding="utf-8") as file:
#     for i in range(len(movie_names)-1, -1, -1):
#         file.write(f"{movie_no-i}: {movie_names[i]}\n")

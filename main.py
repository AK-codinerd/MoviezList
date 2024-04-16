import requests
from bs4 import BeautifulSoup

response = requests.get(
    url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies_page = response.text

soup = BeautifulSoup(movies_page, "html.parser")
# print(soup.prettify())

titles = soup.find(name="div", class_="entity-info-items__list")

movies_in_list = []
anchors = titles.find_all(name="a")
print(anchors)
for tag in anchors:
    new_title = tag["data-test"]
    movies_in_list.append(new_title)

movies = movies_in_list[::-1]  # this will reverse the list
print(movies)

for index, movie in enumerate(movies, 1):  # here it will start the index by looping in the list if you need like i needed it
    # also by passing 1 with the list of movies you can specify from where the list is going to start if i took 3 it would
    # have start from 3 to where the movies are

    with open(file="movies.txt", mode="a") as file:
        file.write(f"{index} : {movie}\n")



# i did this
# num = 1
# for i in range(99, -1, -1):

# ----------here it is as the looping doesn't go to the end so we gotta keep -1 there.. ----------
# ------------it will stop before the final element if you take 0 ------------

#     movie = movies[i]
#     with open(file="movies.txt", mode="a") as file:
#         file.writelines(f"{num}: {movie}\n")
#     num += 1

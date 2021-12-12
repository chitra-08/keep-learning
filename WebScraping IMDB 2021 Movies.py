import requests
from bs4 import BeautifulSoup
import csv

url="https://www.imdb.com/search/title/?year=2021&title_type=feature&"
response = requests.get(url)
mycontent = response.content
soup = BeautifulSoup(mycontent,"html.parser")   
movie_container = soup.findAll('div', attrs={'class': 'lister-item-content'})
movie_list = []
for movie in movie_container:
    movieName = movie.find('a', attrs = {'class':''})
    duration = movie.find('span', attrs = {'class':'runtime'})
    genre = movie.find('span', attrs = {'class':'genre'})
    rating = movie.find('div', attrs = {'class':'inline-block ratings-imdb-rating'})
    cast = movie.find('p', attrs = {'class':''})
    plot1 = movie.findAll('p', attrs = {'class':'text-muted'})[1]
    if rating is not None:
        movie_data = {'Movie Name':movieName.text,'Duration':duration.text,'Genre':genre.text.strip()
                  ,'Rating':rating.text.strip(),'Cast':cast.text.strip(),'Plot':plot1.text.strip()}
    else:
        movie_data = {'Movie Name':movieName.text,'Duration':duration.text,'Genre':genre.text.strip()
            ,'Rating':None,'Cast':cast.text.strip(),'Plot':plot1.text.strip()}
    movie_list.append(movie_data)
for movie in movie_list:
    for k,v in movie.items():
        if k == 'Cast':
            castList = []
            for val in v:
                castList.append(val.replace("\n",""))
            movie.update({'Cast':''.join(castList)})
filename = 'imdb_2021_listing.csv'
with open(filename, 'w', newline='',encoding="utf-8") as f:
    w = csv.DictWriter(f, ['Movie Name', 'Duration', 'Genre','Rating','Cast','Plot'])
    w.writeheader()
    for movie in movie_list:
        w.writerow(movie)
print("File writing completed")

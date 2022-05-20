from pprint import pprint
import requests
import json

TMDB_URL = "https://api.themoviedb.org/3/movie/popular"
API_KEY = "fb6b914b9f73ed0c98e94f8da7d68fb5"
columns = ["genre_ids",'overview','poster_path','release_date','title']


output = []
pk = 0
for page in range(1,4):
    getResponse = requests.request("GET",TMDB_URL, 
    params={
        "api_key":API_KEY,
        'language':"ko",
        'page':page,
        }
    )
    result = getResponse.json()['results']   

    for movie in result:
        pk += 1
        addMovie = {
            "pk":pk,
            "model":"movies.movie"
        }
        for col in columns:
            addMovie[col] = movie[col]
        output.append(addMovie)

pprint(output)
with open("./output.json", 'w', encoding='utf-8') as outfile:
    json.dump(output, outfile, indent=4 ,ensure_ascii=False)
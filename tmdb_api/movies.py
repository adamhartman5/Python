import tmdbsimple as tmdb
from api_key import api_key

tmdb.API_KEY = api_key

search = tmdb.Search()
response = search.movie(query='Lion King')
for s in search.results:
    print(s['title'])
    print(s['vote_average'])
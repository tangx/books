import httpx

MOVIES = "https://tangxin.github.io/moviedux/movies.json"

# with httpx.Client() as client:
#     r = client.get(MOVIES)
#     print(r.status_code)

#     movies = r.json()
#     for movie in movies:
#         print(movie["title"])


c2 = httpx.Client()
try:
    r2 = c2.get(MOVIES)
    print(r2.status_code)
    movies = r2.json()
    for movie in movies:
        print(movie["title"])
finally:
    c2.close()

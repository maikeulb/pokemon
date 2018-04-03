# Pokemon

API client that consumes pokemon data from pokeapi (pokemon API), caches it
with Redis (using redis-py), and measures the response time. 

Technology
----------
* Flask
* Redis

Endpoints
---------

| Method     | URI                                  | Action                                      |
|------------|--------------------------------------|---------------------------------------------|
| `GET`      | `/api/pokemons`                      | `Retrieve all pokemon`<sup>1</sup>          |
| `GET`      | `/api/pokemons/{id}`                 | `Retrieve pokemon`                          |

1. Optional query parameters: limit, offset

Sample Usage
---------------

`http get http://localhost:5000/api/pokemons`
```
{
    "count": 949, 
    "results": [
        {
            "name": "bulbasaur", 
            "url": "https://pokeapi.co/api/v2/pokemon/1/"
        }, 
        {
            "name": "ivysaur", 
            "url": "https://pokeapi.co/api/v2/pokemon/2/"
        }, 
        {
            "name": "venusaur", 
            "url": "https://pokeapi.co/api/v2/pokemon/3/"
        }, 
....
```
logged to console after first request:  
`retrieved pokemons from remote api in 0.62505s ms`

logged to console after second request:  
`retrieved pokemons from cache in 0.00073s ms`

Run
---
If you have docker installed,
```
docker-compose build
docker-compose up
Go to http://localhost:5000 and visit one of the above endpoints
```

Alternatively, open `config.py` and point the Redis URI to your server,
set the `FLASK_APP` env variable to pokemon.py, and pip install the
dependencies (e.g. `pip install -r requirements.txt`). 

`cd` into `./src` (if you are not already) and run the following:
```
flask run
Go to http://localhost:5000 and visit one of the above endpoints
```

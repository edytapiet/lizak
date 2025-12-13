import csv
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


class Movie:
    def __init__(self, movieId: str, title: str, genres: str):
        self.movieId = movieId
        self.title = title
        self.genres = genres


@app.get("/movies")
def get_movies():
    movies_list = []


    try:
        with open('database/movies.csv', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:

                movie = Movie(
                    movieId=row['movieId'],
                    title=row['title'],
                    genres=row['genres']
                )
                movies_list.append(movie)

    except FileNotFoundError:

        return {"error": "Plik movies.csv nie został znaleziony w katalogu database/"}


    return [m.__dict__ for m in movies_list]
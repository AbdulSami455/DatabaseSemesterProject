import uvicorn
from fastapi import FastAPI
import strawberry
from strawberry.asgi import GraphQL
from typing import List


@strawberry.type
class movie:
    title:str
    director:str


@strawberry.type
class query1:
    @strawberry.field
    def movies(self)->List[movie]:
        movies_data=[
            movie(title="Sami", director="nolan"),
        ]
        return movies_data
schema=strawberry.Schema(query=query1)

app = FastAPI()


@app.get("/")
def index():
    return "Hello"


app.add_route("/grapql",GraphQL(schema,debug=True))




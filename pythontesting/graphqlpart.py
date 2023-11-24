import uvicorn
from fastapi import FastAPI
import strawberry
from strawberry.asgi import GraphQL
from typing import List

@strawberry.type
class Movie:
    title: str
    director: str

@strawberry.type
class Query:
    @strawberry.field
    def movies(self) -> List[Movie]:
        movies_data = [
            Movie(title="Sami", director="Nolan"),
        ]
        return movies_data


schema = strawberry.Schema(query=Query)

app = FastAPI()

@app.get("/")
def index():
    return "Hello"

app.add_route("/graphql", GraphQL(schema, debug=True))

#if __name__ == "__main__":
 #   uvicorn.run(app, host="localhost", port=8000, reload=True)

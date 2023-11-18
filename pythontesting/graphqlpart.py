import uvicorn
from  fastapi import FastAPI

app=FastAPI(
    title="Graphql API on Python",
    description="FastApi",
    version="1.3.4"
)

@app.get("/")
def Home():
    return "Welcome Home"

uvicorn.run("graphqlpart:app",host="localhost",port=3400,reload=True)

import uvicorn
from fastapi import FastAPI

app = FastAPI(
    title="GraphQL API on Python",
    description="FastAPI",
    version="1.3.4"
)

@app.get("/")
def home():
    return "Welcome Home"

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=3400, reload=True)

import httpx
import asyncio

async def fetch_graphql_query():
    async with httpx.AsyncClient() as client:
        # Define your GraphQL query
        graphql_query = """
        query {
            movies {
                title
                director
            }
        }
        """

        # Send the GraphQL query to the FastAPI server
        response = await client.post("http://localhost:8000/graphql", json={"query": graphql_query})

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Print the response JSON
            print(response.json())
        else:
            print(f"Error: {response.status_code}, {response.text}")


# Run the asynchronous function to fetch GraphQL data
asyncio.run(fetch_graphql_query())

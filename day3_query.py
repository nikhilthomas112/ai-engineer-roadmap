from fastapi import FastAPI

app = FastAPI()

# A simulated database for testing
fake_items_db = [{"item_name": "Model Weights"}, {"item_name": "API Key"}, {"item_name": "Vector DB"}]

# skip and limit are NOT in the @app.get path, so they become query parameters.
@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10, search: str | None = None):
    # We use 'skip' and 'limit' to slice our list, just like OFFSET and LIMIT in SQL
    results = fake_items_db[skip : skip + limit]
    
    # If the user provides a search term, we return it alongside the data
    if search:
        return {"search_term": search, "results": results}
    
    return {"results": results}


# Run the FastAPI application on port 8000
import uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
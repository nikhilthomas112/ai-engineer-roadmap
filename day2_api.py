from fastapi import FastAPI

# Initialize the core FastAPI application
app = FastAPI()

# The @app.get decorator tells FastAPI: "If someone visits the root URL, run this function."
@app.get("/")
async def read_root():
    return {"message": "Welcome to your first AI Backend Engine!"}

# This is a Path Parameter. We put {item_id} in the URL.
# We enforce type hinting (item_id: int). If a user passes text instead of a number, FastAPI automatically rejects it.
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "status": "Successfully retrieved"}


# Run the FastAPI application on port 8000
import uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
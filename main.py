from fastapi import FastAPI
import requests
from datetime import datetime, timezone

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, Backend Wizard!"}

@app.get("/me")
def get_profile():
    try:
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        response.raise_for_status
        cat_fact = response.json().get("fact", "Could not fetch a cat fact right now.")

    except requests.RequestException:
        # If the request fails (timeout, no internet, API down)
        cat_fact = "Cat fact service unavailable."
    
    timestamp = datetime.now(timezone.utc).isoformat()
    return {
        "status": "success",
        "user": {
            "email": "ebunoluwaigbalaye@gmail.com",
            "name": "Igbalaye Ebunoluwa Kathryn",
            "stack": "Python/FastAPI Backend"
        },
        "timestamp": timestamp,
        "fact": cat_fact
    }
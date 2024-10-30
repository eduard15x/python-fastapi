from fastapi import FastAPI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the TEST_ENV value from the environment
TEST_ENV = os.getenv("TEST_ENV")

# Create an instance of FastAPI
app = FastAPI()

# Define a simple endpoint
@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/greet/{name}")
async def greet_user(name: str):
    return {"message": f"Hello, {name}!", "api_key": TEST_ENV}
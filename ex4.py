import asyncio  # Used to delay for 3 seconds

from fastapi import FastAPI

app = FastAPI()

# Mock database of crew members
crew = [
    {"id": 1, "name": "Cosmo", "role": "Captain"},
    {"id": 2, "name": "Alice", "role": "Engineer"},
    {"id": 3, "name": "Bob", "role": "Scientist"}
]


# Asynchronous endpoint to retrieve all crew members
@app.get("/crew/")
async def get_all_crew_members():
    # Simulate a delay to mimic a time-consuming task
    await asyncio.sleep(3)
    return {"crew": crew}
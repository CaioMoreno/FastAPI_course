from fastapi import FastAPI

app = FastAPI()

# Mock database of crew members
crew = [
    {"id": 1, "name": "Cosmo", "role": "Captain"},
    {"id": 2, "name": "Alice", "role": "Engineer"},
    {"id": 3, "name": "Bob", "role": "Scientist"}
]

@app.delete("/crew/{crew_id}")
async def delete_crew_member(crew_id: int):
    # Find crew member and delete it
    for member in crew:
        if member["id"] == crew_id:
            crew.remove(member)
            return {"message": "Crew member removed"}

    # If the crew member doesn't exist, return a not found message
    return {"message": "Crew member not found"}
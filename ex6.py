from fastapi import FastAPI, Request

app = FastAPI()

# Mock database of crew members
crew = [
    {"id": 1, "name": "Cosmo", "role": "Captain"},
    {"id": 2, "name": "Alice", "role": "Engineer"},
    {"id": 3, "name": "Bob", "role": "Scientist"}
]

@app.put("/crew/{crew_id}")
async def update_crew_member(crew_id: int, request: Request):
    # Parse the incoming JSON request body
    data = await request.json()
    name = data["name"]
    role = data["role"]
    
    # Find crew member and update it
    for member in crew:
        if member["id"] == crew_id:
            member["name"] = name
            member["role"] = role
            return {"crew_id": crew_id, "crew_member": member}

    # If the crew member doesn't exist, return a not found message
    return {"message": "Crew member not found"}
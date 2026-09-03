from fastapi import FastAPI, Request

app = FastAPI()

# Mock database of crew members
crew = [
    {"id": 1, "name": "Cosmo", "role": "Captain"},
    {"id": 2, "name": "Alice", "role": "Engineer"},
    {"id": 3, "name": "Bob", "role": "Scientist"}
]

# Endpoint to add a new crew member using POST method
@app.post("/crew/")
async def add_crew_member(request: Request):
    # Parse the incoming JSON request body
    data = await request.json()
    name = data["name"]
    role = data["role"]
    
    # Create a new ID for the new crew member
    crew_id = max(member["id"] for member in crew) + 1 if crew else 1

    # Add the new member to the mock database
    new_member = {"id": crew_id, "name": name, "role": role}
    crew.append(new_member)

    return {"crew_id": crew_id, "crew_member": new_member}


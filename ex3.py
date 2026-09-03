from fastapi import FastAPI

# Initialize a FastAPI app instance
app = FastAPI()

# Mock database of crew members
crew = [
    {"id": 1, "name": "Cosmo", "role": "Captain"},
    {"id": 2, "name": "Alice", "role": "Engineer"},
    {"id": 3, "name": "Bob", "role": "Scientist"}
]

# Endpoint to get a crew member by path parameter 
@app.get("/crew_path/{crew_id}/{role}") # /crew_path/1/Captain
def read_crew_member_by_path(crew_id: int, role: str):
    for member in crew:
        if member["id"] == crew_id and member["role"] == role:
            return member
    return {"message": "Crew member not found"}

# Endpoint to get a crew member by query parameter 
@app.get("/crew_query/member") # /crew_query/member?crew_id=1&role=Captain
def read_crew_member_by_query(crew_id: int, role: str):
    for member in crew:
        if member["id"] == crew_id and member["role"] == role:
            return member
    return {"message": "Crew member not found"}
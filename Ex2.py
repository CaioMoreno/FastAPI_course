from fastapi import FastAPI

app = FastAPI()

crew = [
    {"id": 1, "name": "Cosmo", "role": "Captain"},
    {"id": 2, "name": "Alice", "role": "Engineer"},
    {"id": 3, "name": "Bob", "role": "Scientist"}
]

@app.get("/crew")
def read_crew():
    return {
                "message": "Success",
                "data": crew
            }
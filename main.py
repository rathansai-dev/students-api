from fastapi import FastAPI

app = FastAPI()

students = [
    {"id": 1, "name": "Rahul"},
    {"id": 2, "name": "Amit"}
]

@app.get("/")
def root():
    return {"message": "Student API"}

@app.get("/students")
def get_students():
    return students
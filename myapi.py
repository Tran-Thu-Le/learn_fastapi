from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel


app = FastAPI() 

students = {
    1: {
        "name": "john",
        "age": 17,
        "year": "12"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

@app.get("/")
def index():
    return students

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, description="The id of student you want to view", gt=0, lt=5)):
    return students[student_id]

@app.get("/get-by-name")
def get_student(name: Optional[str] = None):
    for id in students:
        if students[id]["name"] == name:
            return students[id]
    return {id, "not found"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student_id exists"}

    students[student_id] = student
    return students

@app.put("/update-student/{student_id}")
def create_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student_id does not exists"}

    students[student_id] = student
    return students

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student_id does not exists"}

    del students[student_id]
    return students

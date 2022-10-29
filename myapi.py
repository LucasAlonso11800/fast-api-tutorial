from types import new_class
from fastapi import FastAPI, Path
from typing import Optional
from classes import Student

app = FastAPI()


@app.get('/')
def index():
    return {"name": "First Data"}


students = {
    1: {
        "name": "Someone",
        "age": 17
    },
    2: {
        "name": "Whatever",
        "age": 17
    }
}


@app.get('/student/{student_id}')
def get_student(student_id: int):
    if student_id in students:
        return students[student_id]
    else:
        return {"data": "Not found"}


@app.get('/student-by-name')
def search_student(name: Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"data": "Not found"}


@app.post('/student/{student_id}')
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student already exists"}
    students[student_id] = student
    return students[student_id]

@app.put('/student/{student_id}')
def update_student(student_id: int, student: Student):
    if student_id not in students:
        return {"Error": "Student doesn't exists"}
    students[student_id] = student
    return students[student_id]


@app.delete('/student/{student_id}')
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student doesn't exists"}
    del students[student_id]
    return students
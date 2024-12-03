from fastapi import FastAPI, HTTPException, Query
from models import StudentCreate, StudentUpdate, StudentResponse, StudentListResponse
from config import student_collection
from bson import ObjectId
from typing import List, Optional
import json

app = FastAPI(title="Student Management System")

@app.post("/students", response_model=dict, status_code=201)
async def create_student(student: StudentCreate):
    """
    Create a new student with the provided information.
    All fields (name, age, and address) are mandatory.
    """
    student_dict = student.model_dump()
    result = await student_collection.insert_one(student_dict)
    return {"id": str(result.inserted_id)}

@app.get("/students", response_model=dict)
async def list_students(
    country: Optional[str] = Query(None, description="Filter by country"),
    age: Optional[int] = Query(None, description="Filter by minimum age")
):
    """
    Retrieve a list of students with optional filtering by country and/or minimum age.
    """
    query = {}
    if country:
        query["address.country"] = country
    if age:
        query["age"] = {"$gte": age}

    cursor = student_collection.find(query, {"name": 1, "age": 1, "_id": 0})
    students = await cursor.to_list(length=None)
    return {"data": students}

@app.get("/students/{student_id}", response_model=StudentResponse)
async def get_student(student_id: str):
    """
    Fetch a specific student by their ID.
    Returns 404 if student is not found.
    """
    try:
        student = await student_collection.find_one({"_id": ObjectId(student_id)})
        if student is None:
            raise HTTPException(status_code=404, detail="Student not found")
        student["id"] = str(student.pop("_id"))
        return student
    except:
        raise HTTPException(status_code=404, detail="Student not found")

@app.patch("/students/{student_id}", status_code=204)
async def update_student(student_id: str, student: StudentUpdate):
    """
    Update a student's information by their ID.
    Only provided fields will be updated.
    """
    try:
        update_data = {k: v for k, v in student.model_dump().items() if v is not None}
        if not update_data:
            return

        result = await student_collection.update_one(
            {"_id": ObjectId(student_id)},
            {"$set": update_data}
        )
        
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Student not found")
    except:
        raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/students/{student_id}")
async def delete_student(student_id: str):
    """
    Delete a student by their ID.
    Returns 404 if student is not found.
    """
    try:
        result = await student_collection.delete_one({"_id": ObjectId(student_id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Student not found")
        return {}
    except:
        raise HTTPException(status_code=404, detail="Student not found")

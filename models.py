from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class Address(BaseModel):
    city: str
    country: str

class StudentBase(BaseModel):
    name: str
    age: int
    address: Address

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    address: Optional[Address] = None

class StudentResponse(StudentBase):
    id: str

    class Config:
        json_schema_extra = {
            "example": {
                "id": "507f1f77bcf86cd799439011",
                "name": "John Doe",
                "age": 20,
                "address": {
                    "city": "New York",
                    "country": "USA"
                }
            }
        }

class StudentListResponse(BaseModel):
    name: str
    age: int

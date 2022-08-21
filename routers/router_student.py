from fastapi import APIRouter
from schemas.student import Student
from config.database import connection
from models.student import studentEntity, listOfStudent
from bson import ObjectId

student_router = APIRouter()


@student_router.get('/students')
async def find_all_student():
    return listOfStudent(connection.local.student.find())


@student_router.get("/students/{studentId}")
async def find_student_byId(studentId):
    return studentEntity(connection.local.student.find_one({"_id": ObjectId(studentId)}))


@student_router.post("/students")
async def create_student(student: Student):
    connection.local.student.insert_one(dict(student))
    return listOfStudent(connection.local.student.find())


@student_router.put("/students/{studentId}")
async def update_student(studentId, student: Student):
    connection.local.student.find_one_and_update(
        {"_id": ObjectId(studentId)},
        {"$set": dict(student)}
    )
    return studentEntity(connection.local.student.find_one({"_id": ObjectId(studentId)}))


@student_router.delete("/student/{studentId}")
async def delete_student(studentId):
    return studentEntity(connection.local.student.find_one_and_delete({"_id": ObjectId(studentId)}))

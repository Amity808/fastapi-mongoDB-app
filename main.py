from fastapi import FastAPI
from routers.router_student import student_router

app = FastAPI()

app.include_router(student_router)
# import FastAPI
# FastAPI is the predefined class, used to develop API Calls
from fastapi import FastAPI

# import BaseModel
# BaseModel used to define Schema
from pydantic import BaseModel


# instantiate FastAPI
app = FastAPI()

# Define Schema (Rules & Regulations)
class Employee(BaseModel):
    emp_id:int
    emp_name:str
    department:str
    salary:float
    experience:int
    email:str
    is_active:bool

# DataBase
employees = [{
     "emp_id":111,
     "emp_name":"Emp1",
     "department":"CSE",
     "salary":10000,
     "experience":1,
     "email":"emp1@gmail.com",
     "is_active":True
    }]

@app.get("/")
def home():
    return {"message":"welcome to Fast API !!!"}

@app.get("/employees")
def get_all_employees():
    return {
        "total_employees" : len(employees),
        "data": employees
    }

# req param
@app.get("/employee/{emp_id}")
def get_employee(emp_id:int):
    for emp in employees:
        if emp["emp_id"] == emp_id:
            return emp
    return {"message":"Employee Not Found !!!"}



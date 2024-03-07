
from fastapi import FastAPI

app = FastAPI()

students ={
    1:{
        "name" : "chandhu",
        "age" :19,
        "village" : "jrp"
    }
}
@app.get("/")
async def read_root():
    return {"message": "Hello, World"}


@app.get("/second")
async def write_root():
    return {"this is my first fast api creation"}

@app.get("/third")
async def array():
    return {"id:100,fruits:[banana,grapes,orange],sweets:laddu"}

#  sir sent video based on that
@app.get("/getstudent/{student_id}")
def get_student(student_id : int):
    return students[student_id]
    
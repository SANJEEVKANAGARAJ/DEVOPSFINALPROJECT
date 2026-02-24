from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Backend running successfully"}

@app.get("/student/{name}")
def get_student(name: str):
    return {"student_name": name, "status": "received"}
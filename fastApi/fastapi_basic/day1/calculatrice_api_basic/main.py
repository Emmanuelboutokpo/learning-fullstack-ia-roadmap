from fastapi import FastAPI, HTTPException
app = FastAPI()

@app.get("/add")
def add(a: float, b: float):
    return {"result": a + b}

@app.get("/subtract")
def subtract(a: float, b: float):
    return {"result": a - b}

@app.get("/multiply")
def multiply(a: float, b: float):
    return {"result": a * b}

@app.get("/divide")
def divide(a: float, b: float) -> dict:
    if b == 0:
        raise HTTPException(status_code=400, detail="Division by zero isn't allowed ! ")
    return {"result": a / b}
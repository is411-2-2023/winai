from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/get_customers")
def get_customers():
    return {
        "cus01": "Nice",
        "cus02": "Pim",
    }
from fastapi import FastAPI, HTTPException
from dal.dal import DAL
import uvicorn


app = FastAPI()
DAL = DAL()

@app.get("/get_all_data")
def get_data():
    """
    get all data of database
    """
    try:
        return {"result": DAL.get_all_data()}
    except Exception as e:
        return
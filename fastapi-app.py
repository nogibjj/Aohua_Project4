from fastapi import FastAPI
import uvicorn
#from dblib.querydb import querydb
from readapi import getjson

app = FastAPI()

@app.get("/events")
async def getevents():
    jsondata = getjson()
    return jsondata

@app.get("/")
async def root():
    return {"message": "Hello Databricks"}


@app.get("/subt/{num1}/{num2}")
async def subt(num1: int, num2: int):
    """do subtraction"""

    total = num1 - num2
    return {"result": total}


# @app.get("/query")
# async def query():
#     """Execute a SQL query"""

#     result = querydb()
#     return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
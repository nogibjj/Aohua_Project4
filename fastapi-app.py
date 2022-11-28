from fastapi import FastAPI
import uvicorn
#from dblib.querydb import querydb
from readapi import geteventsasjson, getweather
import json

app = FastAPI()

@app.get("/events")
async def getevents():
    jsondata = geteventsasjson(-1, "", "")
    return jsondata

@app.get("/events/{days}")
async def geteventsindays(days: int):
    jsondata = geteventsasjson(days, "", "")
    return jsondata

@app.get("/events/{days}/{attribute}/{keyword}")
async def geteventsintarget(days: int, attribute: str, keyword: str):
    jsondata = geteventsasjson(days, attribute, keyword)
    return jsondata

@app.get("/")
async def root():
    #return {"message": "Hello Databricks"}
    weatherinfo = getweather()
    # Data to be written 
    dictionary ={ 
        "Greetings": weatherinfo,
        "Check all events": "/events",
        "Check events in future n days": "/events/n",
        "Search target key word in attribute": "/events/n/attribute/keyword"
    } 
        
    # Serializing json  
    return dictionary
    #return {"Greetings": }
    return getweather()


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
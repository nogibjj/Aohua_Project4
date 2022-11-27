# import urllib library
from urllib.request import urlopen
# import json
import json

def getjson():
    # store the URL in url as 
    # parameter for urlopen
    url = "https://calendar.duke.edu/events/index.json?&future_days=30&feed_type=simple"
    # store the response of URL
    response = urlopen(url)
    # storing the JSON response 
    # from url in data
    data_json = json.loads(response.read())
    # print the json response
    return data_json
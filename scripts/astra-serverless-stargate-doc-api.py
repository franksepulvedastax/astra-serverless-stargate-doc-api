# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Astra Cluster ID
astraDbId        = ""
#Astra DB region 
astraRegion      = ""
#Astra DB keyspace
astraKeyspace    = ""
#Astra collection (think of it like a table) to create
astraCollection  = ""
#App token
astraAppToken    = ""

import time
import json 
import requests
from requests.auth import AuthBase

#Json data to load
with open('/Users/franksepulveda/Documents/Astra/astra-serverless-stargate-doc-api/data/MOCK_DATA_PERSON.json') as f:
    people_data = json.load(f)

with open('/Users/franksepulveda/Documents/Astra/astra-serverless-stargate-doc-api/data/MOCK_DATA_CAR.json') as g:
    car_data = json.load(g)

#Required for token authorization
class TokenAuth(AuthBase):
    """Implements a custom authentication scheme."""

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        """Attach an API token to a custom auth header."""
        r.headers['X-Cassandra-Token'] = f'{self.token}'  # Python 3.6+
        return r

###Create collection###
http_request = "https://" + astraDbId + "-" + astraRegion + ".apps.astra.datastax.com/api/rest/v2/namespaces/" + \
    astraKeyspace + "/collections"
headers = {"Content-Type": "application/json", "accept": "application/json"}
response_post_collection = requests.post(http_request, auth=TokenAuth(astraAppToken), params=headers, 
                                         json={"name": astraCollection})
print(response_post_collection) #201 --> Good
print("Collection created...")
time.sleep(15)

###Load documents in to collection (Person)###
http_request = "https://" + astraDbId + "-" + astraRegion + ".apps.astra.datastax.com/api/rest/v2/namespaces/" + \
    astraKeyspace + "/collections/" + astraCollection
headers = {"Content-Type": "application/json", "accept": "application/json"}
for person in people_data:  
    response_collection_to_post_to = requests.post(http_request, auth=TokenAuth(astraAppToken), params=headers, 
                                                   json=person)
    print(response_collection_to_post_to) #201 --> Good  
print("People data loaded...")

###Load documents in to collection (Car)###
http_request = "https://" + astraDbId + "-" + astraRegion + ".apps.astra.datastax.com/api/rest/v2/namespaces/" + \
    astraKeyspace + "/collections/" + astraCollection
headers = {"Content-Type": "application/json", "accept": "application/json"}
for car in car_data:  
    response_collection_to_post_to = requests.post(http_request, auth=TokenAuth(astraAppToken), params=headers, 
                                                   json=car)
    print(response_collection_to_post_to) #201 --> Good
print("Car data loaded...")
import time
import serial
import csv
import string
import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId
from random import randint
from pprint import pprint
client = MongoClient('mongodb+srv://admin:0urtnknM5IpkGQcV@4g06parkme-4gwxq.mongodb.net/test?retryWrites=true')
db=client.ParkMe
collection = db.get_collection('ParkingLots')
id1 = '5c49470d78dea5feb9d02a2c'
spotId1= '5c4946c9ac8f790000f001cf'
collection.update_one({"_id":ObjectId(id1),"parking_spaces.id": ObjectId(spotId1)}, {"$set": {"parking_spaces.$.occupancy": True}})


from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client.chaosHarvester

def save_result(data):
    db.analysis.insert_one(data)
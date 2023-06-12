import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_URI = os.getenv("DBS")

conn = MongoClient(MONGO_URI)
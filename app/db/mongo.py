from pymongo import MongoClient

client = MongoClient('singai-mongo-srv:27017')
db = client["SignAI"]

import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://yunjoo:1234@cluster0.iw1jtaf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = cluster["software_engineering"]

def init_db(app):
    app.config['MONGO_URI'] = "mongodb+srv://yunjoo:1234@cluster0.iw1jtaf.mongodb.net/software_engineering?retryWrites=true&w=majority&appName=Cluster0"
    app.mongo = db

from pymongo import MongoClient
from bson import ObjectId

connection = MongoClient("mongodb+srv://test:test@cluster0.cxhd5.mongodb.net/test?retryWrites=true&w=majority")

LoginDetails_database = connection.get_database('LoginDetails_database')	# to fetch the database

SignUp_collection = LoginDetails_database.Login_record # this is the collection object

def SignUp_insert_data(data):
    document = SignUp_collection.insert_one(data)
    return document.inserted_id


def SignUp_update_or_create(document_id, data):
    document = SignUp_collection.update_one({'_id':ObjectId(document_id)}, {"$set":data}, upsert = True)
    return document.acknowledged 	# return true or false


def SignUp_get_single_data(document_id):
    data = SignUp_collection.find_one({'_id': ObjectId(document_id)})
    return data


def SignUp_all_data():
    data = SignUp_collection.find()
    return list(data)


def SignUp_remove_data(document_id):
    document = SignUp_collection.delete_one({'_id':ObjectId(document_id)})
    return document.acknowledged

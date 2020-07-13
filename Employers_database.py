from pymongo import MongoClient
from bson import ObjectId

connection = MongoClient("mongodb+srv://test:test@cluster0.cxhd5.mongodb.net/test?retryWrites=true&w=majority")

Employers_database = connection.get_database('Employers_DB')	# to fetch the database

Employers_collection = Employers_database.Employers_record # this is the collection object

def Employers_insert_data(data):
	document = Employers_collection.insert_one(data)
	return document.inserted_id

def Employers_update_or_create(document_id, data):
	document = Employers_collection.update_one({'_id':ObjectId(document_id)}, {"$set":data}, upsert = True)
	return document.acknowledged 	# return true or false

def Employers_get_single_data(document_id):
	data = Employers_collection.find_one({'_id': ObjectId(document_id)})
	return data

def Employers_all_data():
	data = Employers_collection.find()
	return list(data)

def Employers_remove_data(document_id):
	document = Employers_collection.delete_one({'_id':ObjectId(document_id)})
	return document.acknowledged

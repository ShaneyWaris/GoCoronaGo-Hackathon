from pymongo import MongoClient
from bson import ObjectId

connection = MongoClient("mongodb+srv://test:test@cluster0.cxhd5.mongodb.net/test?retryWrites=true&w=majority")

Employees_database = connection.get_database('Employees_DB')	# to fetch the database

Employees_collection = Employees_database.Employees_record # this is the collection object

def Employees_insert_data(data):
	document = Employees_collection.insert_one(data)
	return document.inserted_id

def Employees_update_or_create(document_id, data):
	document = Employees_collection.update_one({'_id':ObjectId(document_id)}, {"$set":data}, upsert = True)
	return document.acknowledged 	# return true or false

def Employees_get_single_data(document_id):
	data = Employees_collection.find_one({'_id': ObjectId(document_id)})
	return data

def Employees_all_data():
	data = Employees_collection.find()
	return list(data)

def Employees_remove_data(document_id):
	document = Employees_collection.delete_one({'_id':ObjectId(document_id)})
	return document.acknowledged

def Authentication(email, password):
	try:
		data = dict(Employees_collection.find_one({'Email_id':email}))
		if data['Password'] == password:
			return True, data['Name']
		else:
			return False, "Invalid Password"
	except TypeError:
		return False, "Invalid Email"


from pymongo import MongoClient

class AvesService:
    def __init__(self, db_name='aves', collection_name='pollos'):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def create_ave(self, ave_model):
        ave_data = ave_model.to_dict()
        result = self.collection.insert_one(ave_data)
        return str(result.inserted_id)

    def get_aves(self):
        aves = self.collection.find()
        return list(aves)

    def get_ave_by_id(self, ave_id):
        ave = self.collection.find_one({"_id": ObjectId(ave_id)})
        return ave

    def update_ave(self, ave_id, update_data):
        result = self.collection.update_one({"_id": ObjectId(ave_id)}, {"$set": update_data})
        return result.modified_count > 0

    def delete_ave(self, ave_id):
        result = self.collection.delete_one({"_id": ObjectId(ave_id)})
        return result.deleted_count > 0


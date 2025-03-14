class MongoDBClient:
    def __init__(self, uri, db_name, collection_name):
        from pymongo import MongoClient
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def fetch_all_data(self):
        return list(self.collection.find({}))  # Fetch all documents


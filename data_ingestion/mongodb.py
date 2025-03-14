class MongoDBClient:
    def __init__(self, uri, db_name, collection_name):
        from pymongo import MongoClient
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def fetch_all_data(self):
        return list(self.collection.find({}))  # Fetch all documents



# usag exmaple 
mongo_client = MongoDBClient("mongodb://localhost:27017", "my_database", "my_collection")
data = mongo_client.fetch_all_data()
print(data)  # Output the retrieved documents



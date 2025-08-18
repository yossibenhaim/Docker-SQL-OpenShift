from pymongo import MongoClient
import datetime


class DAL:

    def __init__(self):
        self.client = None

    def connect(self):
        self.client = MongoClient("mongodb://genuser:password@mongodb:27017/namegen")

    def close_conn(self):
        self.client.close()

    def get_all_data(self):
        self.insert_data()
        self.connect()
        collection = self.client.db["posts"]
        data = list(collection.find())
        self.close_conn()
        return data

    def get_data(self):
        return {
            "author": "Mike",
            "text": "My first blog post!",
            "tags": ["mongodb", "python", "pymongo"],
            "date": datetime.datetime.now(tz=datetime.timezone.utc),
        }

    def insert_data(self):
        self.connect()
        post = self.get_data()
        posts = self.client.db["posts"]
        post_id = posts.insert_one(post).inserted_id
        self.close_conn()
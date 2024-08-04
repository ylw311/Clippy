import os
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve credentials from environment variables
username = os.getenv("MONGODB_USERNAME")
password = os.getenv("MONGODB_PASSWORD")
database_name = os.getenv("DATABASE_NAME")
collection_name = os.getenv("COLLECTION_NAME")

def get_mongo_collection():
    uri = f"mongodb+srv://{username}:{password}@hackthe6ix.iw7r6n4.mongodb.net/?retryWrites=true&w=majority&appName=Hackthe6ix"
    print(uri)

    # Create a new client and connect to the server
    client = MongoClient(uri)
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
get_mongo_collection()


import os
from pymongo import MongoClient
from dotenv import load_dotenv

# # Load environment variables from .env file
load_dotenv()

def get_mongo_collection():
    username = os.getenv("MONGODB_USERNAME")
    password = os.getenv("MONGODB_PASSWORD")
    database_name = os.getenv("DATABASE_NAME")
    collection_name = os.getenv("COLLECTION_NAME")

    url = f"mongodb+srv://{username}:{password}@hackthe6ix.iw7r6n4.mongodb.net/?retryWrites=true&w=majority&appName=Hackthe6ix"
    print(url)

    # Create a new client and connect to the server
    client = MongoClient(url)
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    db = client[database_name]
    collection = db[collection_name]
    return collection   


# Test the connection
collection = get_mongo_collection()

if collection is not None:
    print("Successfully obtained collection.")
else:
    print("Failed to obtain collection.")

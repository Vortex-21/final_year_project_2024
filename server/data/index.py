from data_conversion import write_data
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
import json
load_dotenv()
DB_PASSWORD = os.getenv("DB_PASSWORD")
uri = f"mongodb+srv://anshumanlaskar2:{DB_PASSWORD}@cluster0.z6d4m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

def connect():
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
 
def initDB():
    # Initialize collection with data   
    try: 
        collection = client["5g_fraud_detection"]["sim_data"]
        collection.delete_many({})
        write_data()
        with open("sim_data.json","r") as f:
            data = json.load(f)
        collection.insert_many(data)
    except Exception as e:
        print("err: ", e)
if __name__ == "__main__":
    connect()
    initDB()
from motor.motor_asyncio import AsyncIOMotorClient 
import json 


MONGODB_URI="mongodb+srv://sekpeyherbert:pVpYWFiJqUknAmrh@cluster0.bhasa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
database_name = "Meet"


client = AsyncIOMotorClient(MONGODB_URI)
database = client[database_name]
# user_collection = database.get_collection("Books")


user_collection = database["Members"]

with open("users.json") as file:
    data = json.load(file)

user_collection.insert_many(data)

print("done")



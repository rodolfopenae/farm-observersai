from motor.motor_asyncio import AsyncIOMotorClient
from models import DistinctionModel
from bson import ObjectId

MONGO_URI = "mongodb+srv://admin:QvXwKq7WLi27MFj8@cluster.ghxdkmv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster"

client = AsyncIOMotorClient(MONGO_URI)
database = client["observersai"]
distinctions = database.distinctions


async def add(distinction: DistinctionModel):
    new_distinction =  await distinctions.insert_one(distinction)
    created_distinction = await distinctions.find_one({'_id': new_distinction.inserted_id})
    return created_distinction

async def get(id: str):
    distinction = await distinctions.find_one({'_id': ObjectId(id)})
    return distinction

async def update(id: str, data):
    distinction = {k:v for k, v in data.dict().items() if v is not None}
    await distinctions.update_one({'_id': ObjectId(id)}, {'$set': distinction})
    distinction = await distinctions.find_one({'_id': ObjectId(id)})
    return distinction

async def delete(id: str):
    await distinctions.delete_one({'_id': ObjectId(id)})
    return True

async def list():
    all = []
    cursor = distinctions.find({})
    async for distinction in cursor:
        all.append(DistinctionModel(**distinction))
    return all

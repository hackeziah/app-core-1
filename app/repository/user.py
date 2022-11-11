from app.base_model import User
from app.database import database
import uuid


class UserRepo():

    @staticmethod
    async def retrieve():
        _user = []
        collection = database.get_collection('user').find()
        async for user in collection:
            _user.append(user)
        return _user

    @staticmethod
    async def insert(user: User):
        id = str(uuid.uuid4())
        _user = {
            "_id": id,
            "last_name": user.last_name,
            "first_name": user.first_name,
            "email": user.email,
        }
        await database.get_collection('user').insert_one(_user)

    @staticmethod
    async def update(id: str, user: User):
        _user = await database.get_collection('user').find_one({"_id": id})
        _user["last_name"] = user.last_name
        _user["first_name"] = user.first_name
        _user["email"] = user.email
        await database.get_collection('user').update_one({"_id": id}, {"$set": _user})

    @staticmethod
    async def retrieve_id(id: str):
        return await database.get_collection('user').find_one({"_id": id})

    @staticmethod
    async def delete(id: str):
        await database.get_collection('user').delete_one({"_id": id})
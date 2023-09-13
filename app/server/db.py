import motor.motor_asyncio
from decouple import config


MONGO_DETAILS = config("MONGO_DETAILS")  # read env

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.users

user_collection = database.get_collection("users_collection")



# Database
def user_helper(user) -> dict:
    return {
        "user_id": user["id"],
        "name": user["name"],
    }

# retreive all list of users
async def retrieve_users():
    users = []
    async for user in user_collection.find():
        users.append(user_helper(user))
    return users

# create user
async def add_user(user_data: dict) -> dict:
    # Find the maximum existing user_id
    max_user = await user_collection.find_one(sort=[("id", -1)])
    next_user_id = str(int(max_user["id"]) + 1) if max_user and "id" in max_user else "1"

    # Add the new user with the generated user_id
    user_data["id"] = next_user_id
    user = await user_collection.insert_one(user_data)
    new_user = await user_collection.find_one({"id": next_user_id})
    return user_helper(new_user)

# retreive user
async def retrieve_user(user_id: str) -> dict:
    user = await user_collection.find_one({"id": user_id})
    if user:
        return user_helper(user)

# update user
async def update_user(user_id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    user = await user_collection.find_one({"id": user_id})
    if user:
        updated_user = await user_collection.update_one(
            {"id": user_id}, {"$set": data}
        )
        if updated_user:
            return True
    return False

# delete user from db
async def delete_user(user_id: str):
    user = await user_collection.find_one({"id": user_id})
    if user:
        await user_collection.delete_one({"id": user_id})
        return True
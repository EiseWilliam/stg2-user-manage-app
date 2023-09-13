from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from .models.user import (UserCreateSchema, ResponseModel, ErrorResponseModel, UpdateUserModel)
from .db import (add_user,update_user,retrieve_user,retrieve_users,delete_user)

app = FastAPI()

# welcome message
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to user manager app!"}

# CREATE USER ROUTE - add a new user to the collection
@app.post("/api",)
async def add_user_data(user: UserCreateSchema):
    user = jsonable_encoder(user)
    new_user = await add_user(user)
    return ResponseModel(new_user, "User added successfully.")

# UPDATE USER ROUTE - edit the user matching  the id
@app.put("/api/{user_id}",)
async def update_user_data(user_id: str, user: UpdateUserModel):
    user = user.dict(exclude_unset=True)  # Get a dictionary of non-null fields
    if user:
        updated_user = await update_user(user_id, user)
        if updated_user:
            return ResponseModel(user, "User data updated successfully.")
        return ErrorResponseModel("An error occurred", 400, "Error updating user data.")
    return ErrorResponseModel("An error occurred", 400, "No fields to update provided.")

# GET USER ROUTE - retrieve the user matching the id
@app.get("/api/{user_id}", )
async def get_user_data(user_id: str):
    user = await retrieve_user(user_id)
    if user:
        return ResponseModel(user, "User data retrieved successfully.")
    return ErrorResponseModel("User not found", 404, "User with this user_id does not exist.")

# GET ALL ROUTE - retreive all users
@app.get("/api", )
async def get_users():
    users = await retrieve_users()
    if users:
        return ResponseModel(users, "Users data retrieved successfully")
    return ResponseModel(users, "Empty list returned")


# DELETE ROUTE - delete user matching the id
@app.delete("/api/{user_id}",)
async def delete_user_data(user_id: str):
    user = await retrieve_user(user_id)
    deleted_user = await delete_user(user_id)
    if deleted_user:
        return ResponseModel(user, "User data deleted successfully.")
    return ErrorResponseModel("User not found", 404, "User with this user_id does not exist.")

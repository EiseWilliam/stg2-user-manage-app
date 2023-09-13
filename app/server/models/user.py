from typing import Optional

from pydantic import BaseModel, Field

# MODEL
class UserSchema(BaseModel):
    user_id: str
    name: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "user_id": "john_doe",
                "name": "John Doe"
            }
        }

class UserCreateSchema(BaseModel):
    name: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe"
            }
        }

class UpdateUserModel(BaseModel):
    name: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
            }
        }

def ResponseModel( data, message):
    return {
        "data": data,
        200 : message,
    }

def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        code: message,
            }
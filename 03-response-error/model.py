from pydantic import BaseModel
from typing import List

# class Item(BaseModel):
#     item: str
#     status: str


class Todo(BaseModel):
    id: int
    item: str

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "item": "Example schema!"
            }
        }


class TodoItem(BaseModel):
    item: str

    class Config:
        json_schema_extra = {
            "example": {
                "item": "Example schema 1!"
            }
        }


class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        json_schema_extra = {
            "example": {
                "todos": [
                    {"item": "Example schema 1!"},
                    {"item": "Example schema 2!"},
                    {"item": "Example schema 3!"}
                ]
            }
        }

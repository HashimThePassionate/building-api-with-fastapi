from pydantic import BaseModel
from typing import List, Optional
from fastapi import Form

# class Item(BaseModel):
#     item: str
#     status: str


class Todo(BaseModel):
    id: Optional[int] = None
    item: str

    @classmethod
    def as_form(
            cls,
            item: str = Form(...)
    ):
        return cls(item=item)

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

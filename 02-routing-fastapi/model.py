from pydantic import BaseModel


class Item(BaseModel):
    item: str
    status: str


class Todo(BaseModel):
    id: int
    item: Item

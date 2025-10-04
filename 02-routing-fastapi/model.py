from pydantic import BaseModel


# class Item(BaseModel):
#     item: str
#     status: str


class Todo(BaseModel):
    id: int
    item: str

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "item": "Example schema!"
            }
        }

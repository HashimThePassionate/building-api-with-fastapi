from fastapi import APIRouter, Path, HTTPException
from model import Todo, TodoItem, TodoItems
todo_router = APIRouter()

todo_list = []


@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todo() -> dict:
    return {"todos": todo_list}


@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {"message": "Todo added successfully", "todo": todo}


@todo_router.get("/todo/{todo_id}", response_model=TodoItem)
async def get_single_todo(todo_id: int = Path(..., title="The ID  of the todo to retrieve.")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            # Sirf item string return kar rahe hain, ID nahi
            return {"item": todo.item}
    raise HTTPException(status_code=404, detail="Todo with supplied ID does not exist.")


@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="The ID  of the todo to retrieve.")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "Todo with supplied ID does not exist."}

@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {
                "message": "Todo deleted successfully."
            }
    return {
        "message": "Todo with supplied ID doesn't exist."
    }


@todo_router.delete("/todo")
async def delete_all_todo() -> dict:
    todo_list.clear()
    return {
        "message": "Todos deleted successfully."
    }

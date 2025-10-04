# 🚀 **Understanding Routing in FastAPI**

In FastAPI, a **route** is a specific path that is set up to receive requests from a particular **HTTP request method** (like GET or POST). It can also be designed to accept parameters. When your application receives a request, it first checks if a matching route has been defined. If a match is found, the request is passed to a **route handler** for processing.

A **route handler** is simply a function that contains the logic to process an incoming request. For example, a route handler might be a function that connects to a database to fetch specific records when a user sends a request to a particular route.

-----

## 🌐 What are HTTP Request Methods?

**HTTP methods**, also known as HTTP verbs, are identifiers that specify the action a user wants to perform on a resource. The most common methods are:

  * `GET`: To retrieve data.
  * `POST`: To submit new data.
  * `PUT`: To replace existing data entirely.
  * `PATCH`: To apply partial modifications to existing data.
  * `DELETE`: To remove data.

> 📚 You can learn more about all the available HTTP methods on the [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods).

-----

## 📦 Routing with the `APIRouter` Class

The `APIRouter` class is a powerful feature provided by the FastAPI framework. Its main purpose is to help you create path operations for multiple routes in a structured and organized way. Using `APIRouter` is highly encouraged as it promotes modularity, making your application's routing logic clean and easy to manage.

To use it, you first import the `APIRouter` class from the `fastapi` package and create an instance of it. This instance is then used to define all your routes.

### Code Explanation

```python
from fastapi import APIRouter

# Create an instance of the APIRouter
router = APIRouter()

# Define a route using the router instance
@router.get("/hello")
async def say_hello() -> dict:
    return {"message": "Hello!"}
```

  * `from fastapi import APIRouter`: This line imports the necessary `APIRouter` class from the `fastapi` library.
  * `router = APIRouter()`: We create a variable named `router`, which holds an instance of the `APIRouter`. This `router` object will act as a mini FastAPI application, allowing us to define routes on it.
  * `@router.get("/hello")`: This is a decorator that tells FastAPI that the function `say_hello()` below it is responsible for handling `GET` requests sent to the `/hello` path.
  * `async def say_hello() -> dict:`: This defines an asynchronous function named `say_hello` that takes no arguments and is type-hinted to return a dictionary.
  * `return {"message": "Hello!"}`: This is the response that will be sent back to the client as a JSON object.

-----

## 🛠️ Practical Example: Creating and Retrieving Todos

Let's build a practical example by creating a new path operation using `APIRouter` to manage a list of "todos".

### Step 1: Create the `todo.py` File 📁

First, navigate to your project's `todos` folder and create a new Python file named `todo.py`.

```bash
(venv)$ touch todo.py
```

### Step 2: Define the Todo Router and Logic 🧠

We will start by importing `APIRouter` and creating an instance for our todo-related routes.

Inside `todo.py`, add the following code:

```python
from fastapi import APIRouter

# Create a new router instance for todos
todo_router = APIRouter()
```

Next, we will create a temporary in-memory list to act as our database. We will also define two routes: one for adding new todos and another for retrieving them.

```python
# A temporary list to store our todos in memory
todo_list = []

@todo_router.post("/todo")
async def add_todo(todo: dict) -> dict:
    todo_list.append(todo)
    return {"message": "Todo added successfully"}


@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {"todos": todo_list}
```

### Code Explanation

  * `todo_list = []`: We initialize an empty list that will serve as our simple, in-app database to store todo items.
  * `@todo_router.post("/todo")`: This decorator registers the `add_todo` function to handle `POST` requests to the `/todo` endpoint. This is used for creating new todos.
  * `async def add_todo(todo: dict) -> dict:`: This function receives a `todo` item (as a dictionary) in the request body, appends it to our `todo_list`, and returns a success message.
  * `@todo_router.get("/todo")`: This decorator registers the `retrieve_todos` function to handle `GET` requests to the `/todo` endpoint. This is used for fetching all existing todos.
  * `async def retrieve_todos() -> dict:`: This function returns a dictionary containing the entire `todo_list`.

### Step 3: Include the Router in the Main Application 🔗

While `APIRouter` works similarly to the main `FastAPI` class, it cannot be used directly by a server like `uvicorn`. Therefore, we must include the routes defined with `APIRouter` into the main `FastAPI` application instance to make them accessible.

This is done using the `include_router()` method.

> **`include_router(router, ...)`**
> This method is responsible for adding all the path operations defined with an `APIRouter` instance to the main application, making the routes visible and accessible.

Now, open your `api.py` file and modify it to include `todo_router`.

```python
from fastapi import FastAPI
from todo import todo_router

# Create the main FastAPI application instance
app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {
        "message": "Hello World"
    }

# Include the todo routes into the main application
app.include_router(todo_router)
```

### Code Explanation

  * `from todo import todo_router`: We import the `todo_router` instance that we created in the `todo.py` file.
  * `app = FastAPI()`: We create the primary instance of our FastAPI application.
  * `app.include_router(todo_router)`: This crucial line tells our main `app` to incorporate all the routes (`/todo` for `POST` and `GET`) that were defined in the `todo_router`.

### Step 4: Run the Application ▶️

With everything set up, start the Uvicorn server from your terminal.

```bash
(venv)$ uvicorn api:app --port 8000 --reload
```

The command will start the application, and you will see a real-time log of its processes in your terminal.

```text
(venv) ➜ todos git:(main) ✗ uvicorn api:app --port 8000 --reload
INFO:     Will watch for changes in these directories: ['/Users/youngestdev/Work/Building-Web-APIs-with-FastAPI-and-Python/ch02/todos']
INFO:     uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [4732] using statreload
INFO:     Started server process [4734]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### Step 5: Test the Endpoints 🧪

Now, let's test our application by sending requests to the defined routes using `curl`.

#### Test the Root Endpoint (`/`)

First, send a `GET` request to the root URL.

```bash
(venv)$ curl http://127.0.0.1:8000/
```

You should see the "Hello World" message logged in your console.

**✅ Expected Response:**

```json
{"message":"Hello World"}
```

#### Test the `GET /todo` Endpoint

Next, let's check if our todo routes are working by retrieving the list of todos.

```bash
(venv)$ curl -X 'GET' \
  'http://127.0.0.1:8000/todo' \
  -H 'accept: application/json'
```

Since we haven't added any todos yet, the response should be an empty list.

**✅ Expected Response:**

```json
{
  "todos": []
}
```

The todo route is functional\! 🎉

#### Test the `POST /todo` Endpoint

Finally, let's test the `POST` operation by sending a request to add a new item to our todo list.

```bash
(venv)$ curl -X 'POST' \
  'http://127.0.0.1:8000/todo' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 1,
  "item": "First Todo is to finish this book!"
}'
```

**✅ Expected Response:**

You should receive a success message.

```json
{
  "message": "Todo added successfully"
}
```

We have now successfully learned how the `APIRouter` class functions and how to include its routes in the primary application instance. It's important to note that the todo routes we built in this section did not use data models (also known as schemas) for validation.

---


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

# 🛡️ **Validating Request Bodies Using Pydantic Models**

In FastAPI, it's essential to validate the data sent in request bodies. This process, known as **validation**, ensures that your application only receives data in the expected format. It's a crucial security measure that helps sanitize incoming data and reduce the risk of malicious attacks.

A **model** in FastAPI is a class that defines the structure of data, dictating how it should be received and parsed. These models are created by inheriting from Pydantic's `BaseModel` class.

-----

## 📦 What is Pydantic?

**Pydantic** is a powerful Python library designed for data validation and settings management using Python type annotations.

In FastAPI, models defined with Pydantic are used as type hints for request bodies and response objects. This guide will focus on using Pydantic models to validate incoming request bodies.

### Example Pydantic Model

Here is a basic example of a Pydantic model.

```python
from pydantic import BaseModel

class PacktBook(BaseModel):
    id: int
    name: str
    publisher: str
    isbn: str
```

### Code Explanation

  * `from pydantic import BaseModel`: This line imports the core `BaseModel` class from the Pydantic library, which our custom model will inherit from.
  * `class PacktBook(BaseModel):`: We define a new class named `PacktBook` that is a subclass of `BaseModel`. This inheritance gives our class all the data validation powers of Pydantic.
  * `id: int`: This defines a field named `id` that must be an integer.
  * `name: str`, `publisher: str`, `isbn: str`: These lines define three more fields that must all be strings.

Any data object that is type-hinted with the `PacktBook` class must strictly contain these four fields with the specified data types.

-----

## 🛠️ Applying Validation to Our Todo Application

Previously, in our todo application, the route for adding a new item was defined to accept a generic dictionary (`dict`) as the request body.

```python
async def add_todo(todo: dict) -> dict:
    ...
```

The expected data format for a `POST` request was:

```json
{
    "id": 1,
    "item": "My first todo item"
}
```

The major weakness of using `dict` as the type hint is its lack of structure. A user could send an empty dictionary `{}` or a dictionary with completely different keys, and the application would not raise a validation error.

To enforce the correct structure, we can create a Pydantic model that defines exactly what fields are required.

### Step 1: Create a `model.py` File 📁

First, create a new file named `model.py` in your project directory to store your Pydantic models.

### Step 2: Define the `Todo` Model 📝

Inside the new `model.py` file, add the following code to define a model for our todo items.

```python
from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    item: str
```

### Code Explanation

We have created a Pydantic model named `Todo` that will only accept data containing two specific fields:

  * `id`: This field must be an **integer**.
  * `item`: This field must be a **string**.

### Step 3: Update the Route Handler 🔄

Now, let's use our new `Todo` model in the `POST` route.

First, import the `Todo` model into your file containing the router (e.g., `todo.py` or `api.py`).

```python
from model import Todo
```

Next, update the `add_todo` function by replacing the `dict` type hint with our `Todo` model.

```python
todo_list = []

@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {"message": "Todo added successfully"}


@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {"todos": todo_list}
```

By changing `todo: dict` to `todo: Todo`, FastAPI will now automatically validate any incoming request body against the `Todo` model.

### Step 4: Verify the New Validator 🧪

Let's test our updated endpoint to see the validation in action.

#### Test 1: Sending an Invalid Request Body (Empty Dictionary)

We'll use `curl` to send a `POST` request with an empty JSON object.

```bash
(venv)$ curl -X 'POST' \
 'http://127.0.0.1:8000/todo' \
 -H 'accept: application/json' \
 -H 'Content-Type: application/json' \
 -d '{}'
```

**❌ Error Response:**

Because the required fields (`id` and `item`) are missing, FastAPI automatically returns a detailed validation error.

```json
{
  "detail": [
    {
      "loc": [
        "body",
        "id"
      ],
      "msg": "field required",
      "type": "value_error.missing"
    },
    {
      "loc": [
        "body",
        "item"
      ],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

#### Test 2: Sending a Valid Request Body

Now, let's send a request with the correct data structure.

```bash
(venv)$ curl -X 'POST' \
 'http://127.0.0.1:8000/todo' \
 -H 'accept: application/json' \
 -H 'Content-Type: application/json' \
 -d '{
 "id": 2,
 "item": "Validation models help with input types"
}'
```

**✅ Success Response:**

The request body passes validation, and the application returns a successful response.

```json
{
  "message": "Todo added successfully"
}
```

-----

## nesting models

Pydantic models also support nesting, allowing you to build complex data structures.

### Example of a Nested Model

```python
from pydantic import BaseModel

class Item(BaseModel):
    item: str
    status: str

class Todo(BaseModel):
    id: int
    item: Item # The 'item' field is now another Pydantic model
```

With this structure, the expected JSON for a `Todo` object would look like this:

```json
{
    "id": 1,
    "item": {
        "item": "Learn about nested models",
        "status": "completed"
    }
}
```

We have now learned what Pydantic models are, how to create them, and how to use them for robust request body validation in FastAPI.

---


# 🛣️ **Path and Query Parameters**

Following our exploration of Pydantic models for request body validation, this section will introduce **path** and **query** parameters. You will learn what they are, the role they play in API routing, and how to implement them in FastAPI.

-----

## 🔍 Path Parameters

**Path parameters** are variables included directly within the URL path of an API route. They are primarily used to identify a specific resource. Think of them as unique identifiers that help you pinpoint exactly which item you want to interact with in your application.

Our current todo application has routes for adding a todo and retrieving the entire list of todos. Let's expand its functionality by creating a new route that retrieves a *single* todo item by using its ID as a path parameter.

### Implementing a Route with a Path Parameter

We will add a new route to our `todo.py` file to handle fetching a single todo.

```python
from fastapi import APIRouter, Path
from model import Todo

todo_router = APIRouter()

todo_list = []

@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {
        "message": "Todo added successfully."
    }

@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {
        "todos": todo_list
    }

@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="The ID of the todo to retrieve.")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo": todo
            }
    return {
        "message": "Todo with supplied ID doesn't exist."
    }
```

### Code Explanation

  * `@todo_router.get("/todo/{todo_id}")`: This decorator defines the new route. The `{todo_id}` part is the **path parameter**. It acts as a placeholder for the ID of the todo we want to retrieve.
  * `async def get_single_todo(todo_id: int = ...)`: This is the route handler function. The `todo_id` argument in the function corresponds directly to the `{todo_id}` path parameter. The type hint `int` tells FastAPI to convert the path parameter to an integer and validate it.
  * `Path(..., title="...")`: We use FastAPI's `Path` class to provide additional configuration for the path parameter. This helps add more context in the automatically generated API documentation.
  * **Function Logic**: The code iterates through the `todo_list`. If it finds a todo object whose `id` matches the `todo_id` from the URL, it returns that todo. If no match is found after checking the entire list, it returns a "not found" message.

### Testing the Route 🧪

Let's test our new endpoint using `curl`. We will try to retrieve the todo with an ID of `1`.

```bash
(venv)$ curl -X 'GET' \
  'http://127.0.0.1:8000/todo/1' \
  -H 'accept: application/json'
```

In this request, the `1` in the URL `/todo/1` is the value passed as the path parameter. We are asking our application to return the todo item with an ID of `1`.

**✅ Expected Response:**

If a todo with the ID `1` exists, the application will return it.

```json
{
  "todo": {
    "id": 1,
    "item": "First Todo is to finish this book!"
  }
}
```

### The `Path` Class

FastAPI provides a dedicated `Path` class that serves two main purposes:

1.  It helps distinguish path parameters from other arguments that might be present in the route handler function.
2.  It allows you to add more context (like a `title` or `description`) and validation rules, which are then used in the automatic API documentation generated by OpenAPI (visible in tools like Swagger UI and ReDoc).

> ### 💡 Tip: Using `Path(..., kwargs)`
>
> The `Path` class takes a first positional argument that can be set to `None` or an ellipsis (`...`).
>
>   * If the first argument is set to `...` (an ellipsis), the path parameter is marked as **required**.
>   * The `Path` class also accepts keyword arguments for numerical validation. For example, `gt` means **greater than**, and `le` means **less than**. When these are used, FastAPI will automatically validate the path parameter against these rules.
>
> **Example with validation:** `Path(..., gt=0)` would mean the `todo_id` is required and must be greater than 0.

---

# ❓ **Query Parameters**

A **query parameter** is an optional key-value pair that appears in a URL, typically after a question mark (`?`). Its primary purpose is to filter or customize requests, allowing you to retrieve specific data based on the supplied queries.

In a FastAPI route handler, any function argument that does **not** match a path parameter is automatically interpreted as a query parameter. You can also define one explicitly by using an instance of the `Query()` class.

```python
from fastapi import Query

async def query_route(query: str = Query(None)):
    return query
```

> 📚 We will explore advanced use cases for query parameters later on when we build more complex applications.

Now that you've learned how to create routes, validate request bodies, and use parameters, let's see how these components work together.

-----

# 📦 **The Request Body**

In the previous sections, we've seen how to use the `APIRouter` class, validate data with Pydantic models, and handle path parameters. A key component that ties these concepts together is the **request body**.

A **request body** is the data you send *to* your API. It is typically used with routing methods that create or modify data, such as `POST` and `UPDATE`.

> ### 📝 `POST` vs. `UPDATE` Methods
>
>   * The **`POST`** method is used when a new resource is to be inserted or created on the server.
>   * The **`UPDATE`** method (commonly `PUT` or `PATCH`) is used when existing data on the server needs to be modified.

Let's look at the `POST` request we used earlier in the chapter:

```bash
(venv)$ curl -X 'POST' \
 'http://127.0.0.1:8000/todo' \
 -H 'accept: application/json' \
 -H 'Content-Type: application/json' \
 -d '{
 "id": 2,
 "item": "Validation models help with input types"
}'
```

In the command above, the request body is the JSON data sent with the `-d` flag:

```json
{
  "id": 2,
  "item": "Validation models help with input types"
}
```

> ### 💡 Tip: Using the `Body()` Class
>
> FastAPI also provides a `Body()` class, which can be used similarly to `Path()` and `Query()` to add extra validation and metadata to your request bodies.

-----

# 📚 **FastAPI's Automatic API Documentation**

One of FastAPI's most powerful features is its ability to automatically generate documentation for your API. It uses the JSON Schema standard to create definitions for your Pydantic models and documents all your routes, including their path parameters, query parameters, request bodies, and response models.

This documentation is available in two interactive formats by default:

  * **Swagger UI**
  * **ReDoc**

### 🚀 Swagger UI (Interactive Docs)

Swagger UI provides a rich, interactive environment where you can explore and test your API endpoints directly in the browser.

You can access it by navigating to the `/docs` path of your application's URL.

**URL:** `http://127.0.0.1:8000/docs`

The interactive documentation allows you to expand each endpoint, see its details, and even try it out. For example, you can use the interface to add a new todo without needing a tool like `curl`.

### 📜 ReDoc (Detailed Documentation)

ReDoc offers an alternative documentation format that presents a clean, detailed, and well-structured view of your API, models, and routes. It's excellent for a comprehensive overview.

You can access it by navigating to the `/redoc` path of your application's URL.

**URL:** `http://127.0.0.1:8000/redoc`

### ✨ Enhancing Docs with Example Schemas

To make your documentation even more helpful, you can provide example data for your models. This helps users understand exactly what kind of data to send in a request. You can set an example by embedding a `Config` class inside your Pydantic model.

Let's add an example schema to our `Todo` model.

```python
from pydantic import BaseModel

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
```

#### Code Explanation

  * `class Config:`: We create a nested class named `Config` inside our model.
  * `schema_extra`: This is a special property within the `Config` class where you can define extra information for the JSON Schema.
  * `"example": { ... }`: We provide a dictionary under the key `"example"` that contains the sample data for our `Todo` model.

After adding this code and refreshing your documentation pages, the example will appear.

  * In **ReDoc**, when you click on the "Add Todo" endpoint, the example is shown in the right-hand pane, clearly demonstrating the expected request body.

  * In the **Swagger UI**, the example schema will also be visible, guiding users as they test the API.

By adding example schemas, you can guide users on how to properly send requests to your API. The interactive documentation from Swagger serves as a playground for testing, while the detailed documentation from ReDoc acts as a comprehensive knowledge base for using the API.

---
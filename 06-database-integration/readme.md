# 🗄️ **Setting up SQLModel**

To integrate a SQL database into our planner application, the first step is to install the **SQLModel** library. SQLModel is a modern library, built by the creator of FastAPI, that is designed to combine the best of **Pydantic** and **SQLAlchemy**.

## 📦 Installing the SQLModel Library

You can install the library using `pip`:

```bash
pip install sqlmodel
```

Before we dive into adding a database to our planner application, let's explore some of the key methods and concepts from SQLModel that we will use in this section.

## 📜 Tables: Defining Your Data Structure

A **table** is essentially an object that contains all the data for a specific entity, such as our events. The table consists of **columns** (the data attributes, like `title` or `location`) and **rows** (the individual records).

To create a table using SQLModel, you first define a model class. This class inherits from the `SQLModel` base class and includes a special `table` configuration variable set to `True`.

The variables defined in the class will represent the table's columns by default. Let's look at how our `Event` table will be defined:

```python
from typing import Optional, List
from sqlmodel import SQLModel, Field
from sqlalchemy import Column, JSON  # <-- Import Column and JSON

class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    location: str
    tags: List[str] = Field(default=[], sa_column=Column(JSON))
```

### Code Explanation 🧐

  * **`from sqlalchemy import Column, JSON`**: We import `Column` and `JSON` directly from SQLAlchemy. This is necessary because some standard Python types, like `List`, don't have a direct equivalent in all SQL databases.
  * **`class Event(SQLModel, table=True):`**: This line defines our table.
      * It inherits from `SQLModel`, giving it all the Pydantic data validation features and the SQLAlchemy database mapping features.
      * `table=True` explicitly tells SQLModel that this model represents a database table (and not just a data validation model).
  * **`id: Optional[int] = Field(...)`**: This defines our `id` column.
      * `Optional[int]`: The type is an integer, but it's optional because when we create a new event, we won't provide an ID.
      * `Field(default=None, ...)`: We use `Field` to provide extra configuration. `default=None` means the database will be responsible for generating this value.
      * `primary_key=True`: This designates the `id` column as the primary key for this table.
  * **`title: str`, `image: str`, etc.**: These standard class variables are automatically converted by SQLModel into table columns with the appropriate data type (like `VARCHAR`).
  * **`tags: List[str] = Field(...)`**: This is a special column.
      * `sa_column=Column(JSON)`: This is how we handle complex types. `sa_column` stands for "SQLAlchemy Column." Since most SQL databases don't have a native "list of strings" type, we are telling SQLModel to use the `JSON` data type to store our Python list. This is a common and effective solution.

### ❓ What Is a Primary Key?

A **primary key** is a unique identifier for a single record (or row) in a database table. It ensures that every record can be precisely located and that no two records are identical. The `id` is the most common primary key.

## ➡️ Rows: Inserting Data

Data sent to a database table is stored in **rows** under the specified columns. To insert data into the rows, you first create an instance of your table model (just like a Pydantic model) and fill in the variables.

For example, to create a new event, we would first create an instance of the `Event` model:

```python
new_event = Event(title="Book Launch",
                  image="src/fastapi.png",
                  description="The book launch event will be held at Packt HQ, Packt city",
                  location="Google Meet",
                  tags=["packt", "book"])
```

Next, to save this object to the database, you create a database transaction using a `Session`:

```python
with Session(engine) as session:
    session.add(new_event)
    session.commit()
```

The operation above might seem new. Let’s look at what the `Session` class is and what it does.

## 💬 Sessions: The Database Intermediary

A **session** object handles all the interaction between your Python code and the database. It acts as an intermediary for executing operations. The `Session` class takes an instance of a SQL `engine` as its argument (we'll see the `engine` next).

Here are some of the key `session` methods we will be using:

  * **`add(object)`**: This method is responsible for adding a database object (like our `new_event`) to the session's *memory*. The object is now "staged" and is waiting to be committed.
  * **`commit()`**: This method is responsible for "flushing" or saving all staged transactions (like the ones we `add`ed) from the session's memory into the actual database. This makes the changes permanent.
  * **`get(model, id)`**: This method retrieves a *single row* from the database. It takes two parameters: the model class (e.g., `Event`) and the primary key (ID) of the record you want to find.

## 🏁 Creating a Database

Now that we know how to create tables, rows, and sessions, let's look at how the database itself is created.

In SQLModel, connecting to a database is done via a **SQLAlchemy engine**. This engine is created by the `create_engine()` method, which you import from the `sqlmodel` library.

The `create_engine()` method takes the **database URL** as its main argument.

  * The format for a simple SQLite database file is `sqlite:///database.db`.
  * It also takes an optional argument, `echo`. When `echo=True`, it prints all the raw SQL commands it's executing to your console, which is extremely useful for debugging.

However, the `create_engine()` method *alone* isn’t sufficient to create the database file. To create the database *and* all the tables defined in your models, you must also call the `SQLModel.metadata.create_all(engine)` method.

Here is how it all comes together:

```python
from sqlmodel import SQLModel, create_engine

database_file = "database.db"
# Create the engine, telling it to connect to our local SQLite file
engine = create_engine(f"sqlite:///{database_file}", echo=True)

# This is the line that creates the database and tables
SQLModel.metadata.create_all(engine)
```

### Code Explanation 🧐

  * **`SQLModel.metadata.create_all(engine)`**: This powerful method looks at all the classes that inherited from `SQLModel` and had `table=True` (like our `Event` class). It then:
    1.  Creates the `database.db` file if it doesn't already exist.
    2.  Generates and executes the `CREATE TABLE` SQL commands for all found models.

**A crucial note:** The file containing your table definitions (like `models/events.py`) **must be imported** into the file where this database connection code runs *before* you call `create_all()`. If the models aren't imported, SQLModel won't know about them, and no tables will be created.

---

# 🗄️ Integrating SQLModel for Database Operations

In our planner application, we will now perform CRUD (Create, Read, Update, Delete) operations for our events. To do this, we must integrate a database. We will start by creating the file that will manage our database connection.

```bash
touch database/connection.py
```

Now that we have created the database connection file, let’s create the functions and models required to connect our application to the database.

-----

## 1\. Updating the Event Model (`models/events.py`) ✏️

We’ll begin by modifying our original `Event` model class to transform it into a **SQLModel table class**. This class will now define both the API data shape (like Pydantic) and the database table structure (like SQLAlchemy).

```python
from typing import List, Optional
from sqlmodel import JSON, SQLModel, Field, Column

class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True) 
    title: str
    image: str
    description: str
    tags: List[str] = Field(sa_column=Column(JSON))
    location: str

    model_config = {
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event.Ensure to come with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }
    }
```

### Code Explanation 🧐

  * **`from sqlmodel import JSON, SQLModel, Field, Column`**: We import the necessary components from SQLModel. `Column` and `JSON` are imported to handle data types that are not standard in SQL.
  * **`class Event(SQLModel, table=True):`**: This is the key change. By inheriting from `SQLModel` and setting `table=True`, we are instructing SQLModel that this class defines a database table.
  * **`id: Optional[int] = Field(default=None, primary_key=True)`**: We use `Field` to provide extra database configuration.
      * `Optional[int]`: The ID is optional because when we create a *new* event, we won't know the ID; the database will assign it.
      * `default=None`: Tells the database it should be responsible for generating the ID.
      * `primary_key=True`: This designates the `id` column as the unique identifier for this table.
  * **`tags: List[str] = Field(sa_column=Column(JSON))`**: Because most SQL databases do not have a native "list of strings" type, we must provide a special configuration.
      * `sa_column=Column(JSON)`: This tells SQLModel to use the `JSON` data type in the database to store our Python `List`.
  * **`model_config = { ... }`**: This replaces the old nested `class Config`. It's the Pydantic v2 method for setting model configurations.
      * `"arbitrary_types_allowed": True`: This allows for more complex types, often needed for compatibility with SQLAlchemy.
      * `"json_schema_extra": { ... }`: This provides the example data that will be displayed in the API documentation.

-----

## 2\. Creating the EventUpdate Model (`models/events.py`) 🩹

Next, we’ll add another SQLModel class. This model will **not** be a table. Instead, it will be used to validate the data body for our `UPDATE` operations.

```python
class EventUpdate(SQLModel):
    title: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    location: Optional[str] = None
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }
    }
```

### Code Explanation 🧐

  * **`class EventUpdate(SQLModel):`**: Notice this model **does not** include `table=True`. It is only used for data validation, not to define a database table.
  * **`title: Optional[str] = None`**: Every field in this model is `Optional`. This is crucial for `UPDATE` (or `PATCH`) operations, as it allows a user to send a request containing *only* the fields they wish to change, without having to provide all the other fields.

-----

## 3\. Defining the Database Connection (`database/connection.py`) 🔗

Now, let's define the configuration needed to create our database file and establish a connection.

```python
from sqlmodel import SQLModel, Session, create_engine
from models.events import Event

database_file = "planner.db"
database_connection_string = f"sqlite:///{database_file}"

connect_args = {"check_same_thread": False}
engine_url = create_engine(database_connection_string,
                           echo=True, connect_args=connect_args)

def conn():
    SQLModel.metadata.create_all(engine_url)

def get_session():
    with Session(engine_url) as session:
        yield session
```

### Code Explanation 🧐

  * **`from models.events import Event`**: This import is **absolutely essential**. The `conn()` function will only create tables for models that have been imported and read by Python when it's called.
  * **`database_file = "planner.db"`**: This defines the name of our local database file. SQLite is a file-based database.
  * **`database_connection_string = ...`**: This is the standard format for a SQLite connection string.
  * **`connect_args = {"check_same_thread": False}`**: This argument is **required** for using SQLite with FastAPI. By default, SQLite only allows one thread to access it. FastAPI is asynchronous and may use multiple threads. This setting disables that check.
  * **`engine_url = create_engine(...)`**: This creates the main **engine**, which is the core interface to the database.
      * `echo=True`: This is a powerful debugging tool. It will print every raw SQL command that is executed to your console.
      * `connect_args=connect_args`: We pass in our `check_same_thread` setting.
  * **`def conn():`**: We define a simple function that will create our database and tables.
      * `SQLModel.metadata.create_all(engine_url)`: This powerful method searches for all classes that inherited from `SQLModel` and had `table=True` (like our `Event` class) and then generates and executes the `CREATE TABLE` SQL commands.
  * **`def get_session():`**: This is a **dependency generator**. It creates a database session for a single request.
      * `with Session(engine_url) as session:`: This ensures the database connection is properly opened.
      * `yield session`: The `yield` keyword provides this session to the API route that depends on it.
      * After the route is finished, the `with` statement automatically closes the session, preventing database connection leaks.

-----

## 4\. Managing the Application Lifecycle (`main.py`) 🚀

Finally, we need to instruct our application to call the `conn()` function when it starts up. We will use FastAPI's modern `lifespan` event handler for this.

```python
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from database.connection import conn
from routes.users import user_router
from routes.events import event_router
import uvicorn

from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application startup... Database table creating...")
    conn()  # This calls our function to create tables
    yield
    print("Application shutdown...")

app = FastAPI(lifespan=lifespan)

app.include_router(user_router,  prefix="/user")
app.include_router(event_router, prefix="/event")

@app.get("/")
async def home():
    return RedirectResponse(url="/event/")

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
```

### Code Explanation 🧐

  * **`from contextlib import asynccontextmanager`**: We import this to create our `lifespan` context manager.
  * **`@asynccontextmanager async def lifespan(app: FastAPI):`**: This special function defines what FastAPI should do during its startup and shutdown phases.
  * **`print(...)` and `conn()`**: All code *before* the `yield` keyword is executed **once, during application startup**. Here, we print a message and call our `conn()` function to ensure our tables are created.
  * **`yield`**: This keyword separates the startup logic from the shutdown logic.
  * **`print("Application shutdown...")`**: All code *after* the `yield` keyword is executed **once, during application shutdown**.
  * **`app = FastAPI(lifespan=lifespan)`**: We register our `lifespan` function with the main `FastAPI` instance.
  * **`@app.get("/") async def home(): ...`**: This adds a new convenience route. If a user visits the root of our API (`/`), they will be automatically redirected to the `/event/` endpoint.

-----

## 5\. Reviewing the Console Output 📊

When we run `python main.py`, the `lifespan` event and the `echo=True` engine provide detailed console output.

```console
python main.py
INFO:     Will watch for changes in these directories: ['C:\\Users\\Hashim\\Desktop\\resources\\fastapi-api\\06-database-integration']
INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
INFO:     Started reloader process [14900] using WatchFiles
INFO:     Started server process [10328]
INFO:     Waiting for application startup.
Application startup... Database table creating...
2025-10-26 16:08:42,281 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2025-10-26 16:08:42,282 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("event")
2025-10-26 16:08:42,282 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-10-26 16:08:42,283 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("event")
2.283 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-10-26 16:08:42,286 INFO sqlalchemy.engine.Engine 
CREATE TABLE event (
        id INTEGER NOT NULL,
        title VARCHAR NOT NULL,
        image VARCHAR NOT NULL,
        description VARCHAR NOT NULL,
        tags JSON,
        location VARCHAR NOT NULL,
        PRIMARY KEY (id)
)
2025-10-26 16:08:42,286 INFO sqlalchemy.engine.Engine [no key 0.00051s] ()      
2025-10-26 16:08:42,295 INFO sqlalchemy.engine.Engine COMMIT
INFO:     Application startup complete.
INFO:     Shutting down
INFO:     Waiting for application shutdown.
Application shutdown...
INFO:     Application shutdown complete.
INFO:     Finished server process [10328]
INFO:     Stopping reloader process [14900]
```

### Output Explanation 🧐

  * **`Application startup...`**: This is our custom print message from the `lifespan` function, confirming it ran.
  * **`INFO sqlalchemy.engine.Engine ...`**: This block is the output from `echo=True`. It shows SQLModel checking if the `event` table already exists.
  * **`CREATE TABLE event (...)`**: This is the most important part. SQLModel detected the table did not exist and generated and executed the precise SQL command to create our `event` table, perfectly matching our `Event` model.
  * **`INFO sqlalchemy.engine.Engine COMMIT`**: The transaction is committed, and the table is saved in the `planner.db` file.
  * **`Application startup complete.`**: The server is now running and ready to accept requests.
  * **`Application shutdown...`**: These lines appear when you stop the server (e.g., with `CTRL+C`), showing the shutdown part of the `lifespan` function executing correctly.

---

# 🗄️ **Implementing Database-Powered Event Routes**

Now that our database connection is established and our models are defined, we will refactor our event routes to perform full CRUD (Create, Read, Update, Delete) operations by interacting directly with our SQL database.

-----

## ✨ 1. Creating Events

Let's begin by updating our routes file to handle the creation of new events.

### A. Update Imports in `routes/events.py`

First, we must update the imports in `routes/events.py` to include our SQLModel components and the session management function. The `get_session` function is imported so that our routes can access the database session object.

```python
from typing import List
from sqlmodel import Session, select
from database.connection import get_session
from fastapi import APIRouter, HTTPException, status, Depends
from models.events import Event, EventUpdate
```

> ### 💡 What is `Depends`?
>
> The **`Depends`** class is a core part of FastAPI responsible for **Dependency Injection**.
>
> Think of it as a bouncer at a club. Before your route (the party) can start, the bouncer (`Depends`) must check a "truth source" (like our `get_session` function).
>
> `Depends` takes this function as its argument and is passed as a parameter in your route's function. This mandates that the dependency (e.g., "get a valid database session") must be satisfied *before* any of your route's code can be executed. It automatically calls the function, gets the result (the `session`), passes it to your route, and in our case, gracefully closes it afterward.

### B. Update the `POST` Route

Next, let’s update the `POST` route function, `create_event`, to use our database session.

```python
@event_router.post("/new")
async def create_event(new_event: Event, session: Session = Depends(get_session)) -> dict:
    session.add(new_event)
    session.commit()
    session.refresh(new_event)
    return {
        "message": "Event created successfully",
    }
```

#### Code Explanation 🧐

  * **`async def create_event(new_event: Event, session: Session = Depends(get_session))`**:
      * `new_event: Event`: FastAPI validates the incoming JSON body against our `Event` table model.
      * `session: Session = Depends(get_session)`: This is the dependency injection. FastAPI will run the `get_session` function, and the `session` object it `yield`s will be passed to this variable.
  * **`session.add(new_event)`**: This adds the new `new_event` object to the session in memory. It is now "staged" for the database.
  * **`session.commit()`**: This command executes the database transaction, saving the "staged" data to the `event` table.
  * **`session.refresh(new_event)`**: This is a crucial step. When we commit, the database generates the `id` (our primary key). The `new_event` object in our Python code doesn't have this ID yet. `session.refresh()` queries the database *back* for the data we just inserted, "refreshing" our `new_event` object with the new `id`.
  * **`return { ... }`**: We return a success message.

### C. Testing the `POST` Route 🧪

Let’s test the route to preview the changes. If the operation fails, the library will automatically throw an exception.

```bash
curl -X 'POST' 'http://127.0.0.1:8080/event/new' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{"title": "FastAPI Book Launch", "image": "fastapi-book.jpeg", "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!", "tags": ["python", "fastapi", "book", "launch"], "location": "Google Meet"}'
```

A successful response is returned:

```json
{
 "message": "Event created successfully"
}
```

-----

## 📖 2. Read Events

Let’s update the `GET` routes to retrieve data directly from the database instead of the in-memory list.

### A. Retrieve All Events

```python
@event_router.get("/", response_model=List[Event])
async def retrieve_all_events(session: Session = Depends(get_session)) -> List[Event]:
    statement = select(Event)
    events = session.exec(statement).all()
    return events
```

#### Code Explanation 🧐

  * **`session: Session = Depends(get_session)`**: Just like before, we use dependency injection to get a database session.
  * **`statement = select(Event)`**: This creates a SQLModel `SELECT` statement. It's the equivalent of `SELECT * FROM event`.
  * **`events = session.exec(statement).all()`**: This line executes the `SELECT` statement.
      * `session.exec(statement)` runs the query.
      * `.all()` fetches all results and returns them as a list of `Event` objects.
  * **`return events`**: The list of events is returned. `response_model=List[Event]` ensures they are serialized correctly as JSON.

### B. Retrieve a Single Event

Likewise, the route to display an event’s data when retrieved by its ID is also updated.

```python
@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: int, session: Session = Depends(get_session)) -> Event:
    event = session.get(Event, id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    return event
```

#### Code Explanation 🧐

  * **`event = session.get(Event, id)`**: This is the most efficient way to get a single item by its primary key. We ask the `session` to `get` an object of type `Event` with the primary key `id`.
  * **`if not event:`**: If `session.get` returns `None` (meaning no event with that ID was found), this check will be true.
  * **`raise HTTPException(...)`**: We immediately stop and return a `404 NOT_FOUND` error, as defined in our logic.
  * **`return event`**: If the event is found, it is returned.

### C. Testing the `GET` Routes 🧪

Let’s test both routes by first sending a `GET` request to retrieve the list of all events.

```bash
curl -X 'GET' \
 'http://127.0.0.1:8080/event/' \
 -H 'accept: application/json'
```

We get a response containing the event we created:

```json
[
 {
 "id": 1,
 "title": "FastAPI Book Launch",
 "image": "fastapi-book.jpeg",
 "description": "We will be discussing the contents of the FastAPI book in this event.Ensure to come with your own copy to win gifts!",
 "tags": [
 "python",
 "fastapi",
 "book",
 "launch"
 ],
 "location": "Google Meet"
 }
]
```

Next, let’s retrieve the event by its ID:

```bash
curl -X 'GET' \
 'http://127.0.0.1:8080/event/1' \
 -H 'accept: application/json'
```

```json
{
 "id": 1,
 "title": "FastAPI Book Launch",
 "image": "fastapi-book.jpeg",
 "description": "The launch of the FastAPI book will hold on xyz.",
 "tags": [
 "python",
 " fastapi"
 ],
 "location": "virtual"
}
```

With the READ operations successfully implemented, let’s add an edit feature.

-----

## ✏️ 3. Update Events

Let’s add the `UPDATE` route in `routes/events.py`.

```python
@event_router.put("/edit/{id}", response_model=Event)
async def update_event(id: int, new_data: EventUpdate, session: Session = Depends(get_session)) -> Event:
    event = session.get(Event, id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )

    event_data = new_data.model_dump(exclude_unset=True)

    for key, value in event_data.items():
        setattr(event, key, value)

    session.add(event)
    session.commit()
    session.refresh(event)
    return event
```

#### Code Explanation 🧐

  * **`async def update_event(id: int, new_data: EventUpdate, ...)`**:
      * `id: int`: We get the ID of the event to update from the URL path.
      * `new_data: EventUpdate`: We use our `EventUpdate` model to validate the request body. This model has all optional fields.
  * **`event = session.get(Event, id)`**: We first fetch the event from the database.
  * **`if not event:`**: We raise a `404` error if the event doesn't exist.
  * **`event_data = new_data.model_dump(exclude_unset=True)`**: This is the magic for partial updates (PATCH).
      * `new_data.model_dump()` creates a dictionary from the `new_data` model.
      * `exclude_unset=True` tells Pydantic to *only* include fields that the client *actually sent* in the JSON request. Any fields the client omitted will not be in this dictionary, so we don't accidentally overwrite existing data with `None`.
  * **`for key, value in event_data.items():`**: We loop through the dictionary of *only the provided fields*.
  * **`setattr(event, key, value)`**: This dynamically updates the `event` object we fetched from the database. `setattr(event, "title", "New Title")` is the same as `event.title = "New Title"`.
  * **`session.add(event)`**: We add the *updated* `event` object back to the session.
  * **`session.commit()`**: We save the changes to the database.
  * **`session.refresh(event)`**: We refresh the `event` object to get the definitive state from the database.
  * **`return event`**: The fully updated event object is returned.

### Testing the `PUT` Route 🧪

Let’s update the existing event’s title:

```bash
curl -X 'PUT' \
 'http://127.0.0.1:8080/event/edit/1' \
 -H 'accept: application/json' \
 -H 'Content-Type: application/json' \
 -d '{
 "title": "Packt'\''s FastAPI book launch II"
}'
```

The response shows the updated data:

```json
{
 "id": 1,
 "title": "Packt's FastAPI book launch II",
 "image": "fastapi-book.jpeg",
 "description": "The launch of the FastAPI book will hold on xyz.",
 "tags": ["python", "fastapi"],
 "location": "virtual" 
}
```

-----

## 🗑️ 4. Delete Event

Now that we have added the update functionality, let’s quickly add a delete operation. In `events.py`, update the delete route.

```python
@event_router.delete("/delete/{id}")
async def delete_event(id: int, session: Session = Depends(get_session)) -> dict:
    event = session.get(Event, id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    session.delete(event)
    session.commit()
    return {"message": "Event deleted successfully"}
```

#### Code Explanation 🧐

  * **`event = session.get(Event, id)`**: We fetch the event by its ID.
  * **`if not event:`**: We check if it exists and return a `404` if not.
  * **`session.delete(event)`**: We mark the fetched event for deletion within the session.
  * **`session.commit()`**: We execute the `DELETE` command in the database, making the deletion permanent.
  * **`return { ... }`**: A success message is returned.

### Testing the `DELETE` Route 🧪

Let’s delete the event from the database:

```bash
curl -X 'DELETE' \
 'http://127.0.0.1:8080/event/delete/2' \
 -H 'accept: application/json'
```

The request returns a successful response:

```json
{
 "message": "Event deleted successfully"
}
```

Now, if we retrieve the list of events, we get an empty array for a response:

```bash
curl -X 'GET' \
 'http://0.0.0.0:8080/event/' \
 -H 'accept: application/json'
```

```json
[]
```

---
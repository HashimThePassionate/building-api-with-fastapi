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
# 🏗️ **Structuring FastAPI Applications**

In the previous chapters, we explored the fundamentals of creating a FastAPI application. The single-file to-do app we built demonstrated the remarkable flexibility and power of FastAPI, highlighting how easy it is to get started.

However, as applications grow in complexity and gain more features, a single-file structure becomes difficult to maintain. This is where the need for proper application structuring becomes essential.

**Structuring** refers to the arrangement of an application's components in an organized and modular format. This separation of concerns is vital for improving the readability of your code and content.

A well-structured application leads to:

  * 🚀 Faster development
  * 🐛 Quicker debugging
  * 📈 An overall increase in productivity

This chapter will equip you with the knowledge of what structuring is and how to effectively structure your API. We will cover structuring application routes and models, and implement the models for a new "planner" API.

-----

## 🏛️ Structuring in FastAPI Applications

For this chapter, we will begin building a new event planner application. We'll name the project `05-structuring-apps`.

Let's design our target application structure to look like this:

```plaintext
05-structuring-apps/
├── main.py
├── database/
│   ├── __init__.py
│   └── connection.py
├── routes/
│   ├── __init__.py
│   ├── events.py
│   └── users.py
└── models/
    ├── __init__.py
    ├── events.py
    └── users.py
```

### 1\. Create the Project Directory

The first step is to create a new folder for our application.

```bash
mkdir 05-structuring-apps && cd 05-structuring-apps
```

#### 📜 Command Explanation

  * **`mkdir 05-structuring-apps`**: This command creates a new directory named `05-structuring-apps`.
  * **`&&`**: This is a logical operator that chains commands. It means "if the first command was successful, then run the next command."
  * **`cd 05-structuring-apps`**: This command changes the current directory, moving you inside the newly created project folder.

-----

### 2\. Create the Entry File and Subfolders

Inside our new project directory, we will create the main entry file (`main.py`) and three subfolders to organize our code.

```bash
touch main.py
mkdir database routes models
```

#### 📜 Command Explanation

  * **`touch main.py`**: This command creates a new, empty file named `main.py`. This file will be the main entry point for our application.
  * **`mkdir database routes models`**: This command creates three new sub-directories simultaneously: `database`, `routes`, and `models`.

-----

### 3\. Initialize Folders as Python Packages

Next, we must create an `__init__.py` file in every folder we just made. This is a special file that tells Python to treat these directories as packages (modules), allowing us to import files from them.

```bash
touch {database,routes,models}/__init__.py
```

#### 📜 Command Explanation

  * **`touch ...`**: This command creates the empty `__init__.py` files.
  * **`{database,routes,models}/`**: This is a shell expansion. The command will run for each item inside the curly braces, effectively running:
      * `touch database/__init__.py`
      * `touch routes/__init__.py`
      * `touch models/__init__.py`

-----

### 4\. Set Up the Database Folder

In the `database` folder, let's create a file that will handle our database configurations and connection logic in the future.

```bash
touch database/connection.py
```

#### 📜 Command Explanation

  * This command creates a new, empty file named `connection.py` inside the `database` directory. This file will later contain all our database abstraction and configuration logic.

-----

### 5\. Create Feature-Specific Files

Finally, we'll create the files for our specific API features (events and users) inside both the `routes` and `models` folders.

```bash
touch {routes,models}/{events,users}.py
```

#### 📜 Command Explanation

  * This command uses shell expansion twice to create multiple files at once. It expands to:
      * `touch routes/events.py`
      * `touch routes/users.py`
      * `touch models/events.py`
      * `touch models/users.py`

-----

## 📦 Understanding the File Responsibilities

We have now successfully structured our API by grouping similar files according to their functions. Each file has a distinct purpose:

### 📁 `routes/`

Files in this folder will define the API endpoints (paths) for different features.

  * **`events.py`**: This file will handle all routing operations for events, such as creating, updating, and deleting them.
  * **`users.py`**: This file will handle all routing operations for users, such as registration and sign-in.

### 📁 `models/`

Files in this folder will contain the Pydantic model definitions (the data shapes) for our application.

  * **`events.py`**: This file will contain the Pydantic models required for event operations (e.g., `EventCreate`, `EventUpdate`).
  * **`users.py`**: This file will contain the Pydantic models required for user operations (e.g., `UserCreate`, `UserLogin`).

---
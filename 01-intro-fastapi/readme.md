#  **Building a Simple FastAPI Application**

<details>
<summary>📋 Table of Contents</summary>

- [**Building a Simple FastAPI Application**](#building-a-simple-fastapi-application)
    - [📦 Step 1: Install Dependencies](#-step-1-install-dependencies)
    - [🐍 Step 2: Create the FastAPI Instance and First Route](#-step-2-create-the-fastapi-instance-and-first-route)
      - [Code Explanation ⚙️](#code-explanation-️)
    - [▶️ Step 3: Run the Application](#️-step-3-run-the-application)
      - [Command Arguments Explained](#command-arguments-explained)
    - [🧪 Step 4: Test the Application](#-step-4-test-the-application)

</details>

<br/>

This guide will walk you through creating your very first project with FastAPI. The goal is to introduce the framework by building a basic application. More advanced features will be covered later.

### 📦 Step 1: Install Dependencies

First, we need to install the necessary packages for our application inside the `todos` folder you created earlier.

The required dependencies are:

  * **fastapi**: The main framework we will use to build our API.
  * **uvicorn**: An Asynchronous Server Gateway Interface (ASGI) server that will run our application.

Let's begin by activating your virtual development environment. Open your terminal in the project directory and run this command:

```bash
$ source venv/bin/activate
```

Once the environment is active, install the dependencies using `pip`:

```bash
(venv)$ pip install fastapi uvicorn
```

-----

### 🐍 Step 2: Create the FastAPI Instance and First Route

Now, let's write some code\!

1.  Create a new file named `api.py`.
2.  Inside `api.py`, create a new instance of the `FastAPI` class:

<!-- end list -->

```python
from fastapi import FastAPI

app = FastAPI()
```

By creating the `app` variable, which holds our `FastAPI` instance, we can now define routes for our application.

A **route** is created by using a decorator to specify the HTTP method (`GET`, `POST`, etc.) and the URL path. This is followed by a function that contains the logic to be executed when that route is requested.

Let's create a welcome route at the root path (`/`) that accepts `GET` requests and returns a simple welcome message.

Add the following code to your `api.py` file:

```python
@app.get("/")
async def welcome() -> dict:
 return { "message": "Hello World"}
```

#### Code Explanation ⚙️

  * `@app.get("/")`: This is a **decorator** that tells FastAPI that the function right below it is responsible for handling `GET` requests that come to the root URL (`/`).
  * `async def welcome() -> dict:`: This defines an **asynchronous function** named `welcome`. The `-> dict` is a Python type hint, indicating that this function will return a dictionary.
  * `return { "message": "Hello World"}`: This is the content that will be returned. FastAPI automatically converts this Python dictionary into a JSON response.

-----

### ▶️ Step 3: Run the Application

The next step is to start our application using the **uvicorn** server. In your terminal, run the following command:

```bash
(venv)$ uvicorn api:app --port 8000 --reload
```

#### Command Arguments Explained

  * **`api:app`**: This tells uvicorn where to find the FastAPI instance.
      * `api`: Refers to the `api.py` file.
      * `app`: Refers to the `app = FastAPI()` object created inside that file.
  * **`--port 8000`**: This specifies that the application should be served on port `8000`.
  * **`--reload`**: This is a helpful optional argument for development. It automatically restarts the server whenever you save a change in your file.

After running the command, you will see output in your terminal similar to this:

```console
(venv) ➜ todos uvicorn api:app --port 8000 --reload
INFO:     Will watch for changes in these directories: ['/Users/youngestdev/Documents/todos']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [3982] using statreload
INFO:     Started server process [3984]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

-----

### 🧪 Step 4: Test the Application

Finally, let's test that our application is working correctly. Open a **new terminal window** (leave the uvicorn server running in the first one) and send a `GET` request to the API using `curl`.

```bash
$ curl http://127.0.0.1:8000/
```

The application will respond with the JSON message we defined. You will see the following output in your console:

```json
{"message":"Hello World"}
```

Congratulations\! You have successfully built and tested your first FastAPI application. 🎉
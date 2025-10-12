# 🎨 **Jinja The Python Templating Engine**

<details>
<summary><strong>📚 Table of Contents</strong></summary>

### 📋 **Navigation**

#### **🧱 Jinja Fundamentals**
- [🧱 Core Syntax Blocks](#-core-syntax-blocks)
- [✨ Key Features of Jinja](#-key-features-of-jinja)
  - [💧 Filters: Modifying Your Data](#-filters-modifying-your-data)
    - [The `default` Filter](#the-default-filter)
    - [The `escape` Filter](#the-escape-filter)
    - [Conversion Filters (`int` and `float`)](#conversion-filters-int-and-float)
    - [The `join` Filter](#the-join-filter)
    - [The `length` Filter](#the-length-filter)
  - [🧠 Control Structures: Adding Logic to Templates](#-control-structures-adding-logic-to-templates)
  - [🧩 Macros: Reusable Template Functions](#-macros-reusable-template-functions)
  - [🏛️ Template Inheritance: The DRY Principle in Action](#️-template-inheritance-the-dry-principle-in-action)

#### **🚀 FastAPI Integration**
- [🎨 **Jinja The Python Templating Engine**](#-jinja-the-python-templating-engine)
    - [📋 **Navigation**](#-navigation)
      - [**🧱 Jinja Fundamentals**](#-jinja-fundamentals)
      - [**🚀 FastAPI Integration**](#-fastapi-integration)
  - [🧱 Core Syntax Blocks](#-core-syntax-blocks)
  - [✨ Key Features of Jinja](#-key-features-of-jinja)
    - [💧 Filters: Modifying Your Data](#-filters-modifying-your-data)
      - [The `default` Filter](#the-default-filter)
      - [The `escape` Filter](#the-escape-filter)
      - [Conversion Filters (`int` and `float`)](#conversion-filters-int-and-float)
      - [The `join` Filter](#the-join-filter)
      - [The `length` Filter](#the-length-filter)
    - [🧠 Control Structures: Adding Logic to Templates](#-control-structures-adding-logic-to-templates)
      - [`if` Statements](#if-statements)
      - [Loops](#loops)
    - [🧩 Macros: Reusable Template Functions](#-macros-reusable-template-functions)
    - [🏛️ Template Inheritance: The DRY Principle in Action](#️-template-inheritance-the-dry-principle-in-action)
- [🚀 **Using Jinja Templates in FastAPI to Build a Web Interface**](#-using-jinja-templates-in-fastapi-to-build-a-web-interface)
  - [Setting the Stage 🎬](#setting-the-stage-)
    - [1. Initial Setup: Installing Jinja and Creating the Templates Directory 📁](#1-initial-setup-installing-jinja-and-creating-the-templates-directory-)
    - [2. Creating the HTML Template Files 📄](#2-creating-the-html-template-files-)
    - [3. Configuring Jinja within the FastAPI Application ⚙️](#3-configuring-jinja-within-the-fastapi-application-️)
      - [A. Updating the API Routes in `todo.py`](#a-updating-the-api-routes-in-todopy)
      - [Code Explanation 🧐](#code-explanation-)
      - [B. Updating the Pydantic Model in `model.py`](#b-updating-the-pydantic-model-in-modelpy)
      - [Code Explanation 🧐](#code-explanation--1)
    - [4. Crafting the Base Template: `home.html` 🏛️](#4-crafting-the-base-template-homehtml-️)
      - [Code Explanation 🧐](#code-explanation--2)
    - [5. Running the Application and First Preview 🌐](#5-running-the-application-and-first-preview-)
    - [6. Creating the Child Template: `todo.html` 🧩](#6-creating-the-child-template-todohtml-)
      - [Code Explanation 🧐](#code-explanation--3)
    - [7. Final Verification: A Complete Walkthrough ✅](#7-final-verification-a-complete-walkthrough-)

---

</details>

<br/>

**Jinja** is a modern and powerful templating engine written in Python. Its primary purpose is to facilitate the rendering process of responses, allowing developers to dynamically generate content like HTML, XML, or other text-based formats.

In any templating language, there are two fundamental concepts:

  * **Variables**: These are placeholders that get replaced with actual values when the template is rendered.
  * **Tags**: These control the logic of the template, such as loops and conditional statements.

Jinja uses curly bracket syntax `{}` to distinguish its expressions from the static text or HTML in a template file.

-----

## 🧱 Core Syntax Blocks

Jinja employs three primary syntax blocks to handle different tasks within a template.

  * `{% ... %}` - **Statements**: This syntax is used for control structures like `if` statements and `for` loops.
  * `{{ ... }}` - **Expressions**: This block is used to print the output of an expression or the value of a variable directly into the template. For example, `{{ todo.item }}` would display the value of the `item` attribute from the `todo` object.
  * `{# ... #}` - **Comments**: This syntax is used for writing comments. Anything inside these blocks will not be included in the final rendered output. For example: `{# This is a great API book! #}`.

You can pass various Python data types as variables to a Jinja template—including models, lists, or dictionaries—as long as they can be converted into strings for display.

Next, we will explore some of the most common and powerful features used in Jinja.

-----

## ✨ Key Features of Jinja

### 💧 Filters: Modifying Your Data

While Jinja's syntax is similar to Python's, you cannot use standard Python syntax for data manipulation directly within a template (e.g., calling string methods). To perform modifications like joining strings or capitalizing text, Jinja provides **filters**.

A filter is applied to a variable using a pipe symbol (`|`). Some filters may also accept optional arguments in parentheses.

**Syntax with arguments:**

```jinja
{{ variable | filter_name(*args) }}
```

**Syntax without arguments:**

```jinja
{{ variable | filter_name }}
```

Let's look at some common built-in filters.

#### The `default` Filter

This filter provides a fallback value to display if the variable is undefined or `None`.

**Code:**

```jinja
{{ todo.item | default('This is a default todo item') }}
```

**Output:**

```
This is a default todo item
```

#### The `escape` Filter

This filter escapes a string for safe inclusion in HTML, which helps prevent Cross-Site Scripting (XSS) attacks by converting special characters like `<` and `>` into their HTML entity equivalents.

**Code:**

```jinja
{{ "<p>Hello</p>" | escape }}
```

**Output:**

```html
&lt;p&gt;Hello&lt;/p&gt;
```

#### Conversion Filters (`int` and `float`)

These filters are used to convert a value to an integer or a floating-point number.

**Code:**

```jinja
{{ 3.142 | int }}
{{ 31 | float }}
```

**Output:**

```
3
31.0
```

#### The `join` Filter

This filter joins the elements of a list into a single string, using an optional separator.

**Code:**

```jinja
{{ ['Packt', 'produces', 'great', 'books!'] | join(' ') }}
```

**Output:**

```
Packt produces great books!
```

#### The `length` Filter

This filter returns the number of items in an object, similar to Python's built-in `len()` function.

**Code:**

```jinja
Todo count: {{ todos | length }}
```

**Output (assuming `todos` has 4 items):**

```
Todo count: 4
```

> **Note:** For a complete list of built-in filters and more advanced usage, please refer to the [official Jinja documentation](https://www.google.com/search?q=https://jinja.palletsprojects.com/en/3.1.x/templates/%23builtin-filters).

-----

### 🧠 Control Structures: Adding Logic to Templates

#### `if` Statements

The usage of `if` statements in Jinja is very similar to Python and allows for conditional rendering of content. These statements are written inside `{% ... %}` control blocks.

**Example:**

```jinja
{% if todos | length < 5 %}
  You don't have many items on your todo list!
{% else %}
  You have a busy day it seems!
{% endif %}
```

#### Loops

You can iterate over sequences like lists or dictionaries using a `for` loop, just as you would in Python.

**Example:**

```jinja
{% for todo in todos %}
  {{ todo.item }} 
{% endfor %}
```

Inside a `for` loop, Jinja provides access to special variables that give information about the state of the loop.

| Variable | Description |
| :--- | :--- |
| `loop.index` | The current iteration of the loop (1-indexed). |
| `loop.index0` | The current iteration of the loop (0-indexed). |
| `loop.revindex` | The number of iterations from the end of the loop (1-indexed). |
| `loop.revindex0` | The number of iterations from the end of the loop (0-indexed). |
| `loop.first` | `True` if this is the first iteration. |
| `loop.last` | `True` if this is the last iteration. |
| `loop.length` | The total number of items in the sequence. |
| `loop.cycle` | A helper function to cycle through a list of strings. |
| `loop.depth` | The current depth in a recursive loop (starts at 1). |
| `loop.depth0` | The current depth in a recursive loop (starts at 0). |
| `loop.previtem` | The item from the previous iteration (undefined on the first iteration). |
| `loop.nextitem` | The item from the next iteration (undefined on the last iteration). |
| `loop.changed(*val)`| `True` if its arguments have changed from the last iteration. |

-----

### 🧩 Macros: Reusable Template Functions

A **macro** in Jinja is comparable to a function in a programming language. It allows you to define reusable pieces of template code to avoid repetition. A macro's main purpose is to render a reusable chunk of HTML.

For instance, you can define a macro to generate HTML `<input>` tags consistently across a form.

**Defining the Macro:**

```jinja
{% macro input(name, value='', type='text', size=20) %}
  <input type="{{ type }}" name="{{ name }}" value="{{ value }}" size="{{ size }}">
{% endmacro %}
```

**Calling the Macro:**
Now, you can easily create an input field by calling the macro.

```jinja
{{ input('item') }}
```

**Resulting HTML:**

```html
<input type="text" name="item" value="" size="20">
```

-----

### 🏛️ Template Inheritance: The DRY Principle in Action

Perhaps the most powerful feature of Jinja is **template inheritance**. This feature is a direct application of the "Don't Repeat Yourself" (DRY) principle and is incredibly useful in large web applications.

Template inheritance allows you to create a base template (or "skeleton") that contains the common elements of your site. Child templates can then **inherit** from this base template and **override** specific sections, or blocks, with their own content.

> **Note:** To learn more about how to structure and use template inheritance, visit the [official Jinja documentation](https://www.google.com/search?q=https://jinja.palletsprojects.com/en/3.1.x/templates/%23template-inheritance).


---

# 🚀 **Using Jinja Templates in FastAPI to Build a Web Interface**

In this guide, we will transition our to-do API from serving JSON data to rendering dynamic HTML pages using the **Jinja2** templating engine. This will allow us to create a user-friendly web interface for our application.

## Setting the Stage 🎬

Before we write any code, we need to prepare our project. This involves installing the Jinja2 package and creating a dedicated directory to store our template files.

Our template files will be standard HTML mixed with Jinja's special syntax for embedding logic and variables. For styling, we will leverage the **Bootstrap CSS library**, which will be loaded directly from a CDN (Content Delivery Network). This allows us to focus on the application's functionality rather than writing custom CSS. Any extra assets like custom stylesheets or JavaScript files could be stored in a separate folder, a topic we will explore when discussing static files.

-----

### 1\. Initial Setup: Installing Jinja and Creating the Templates Directory 📁

First, we need to add Jinja2 to our project's dependencies and create a folder named `templates`. FastAPI will look inside this folder for our HTML files.

Execute the following commands in your terminal while your virtual environment is active:

```bash
# Install the Jinja2 package
pip install jinja2

# Create the templates directory
mkdir templates
```

-----

### 2\. Creating the HTML Template Files 📄

Inside the newly created `templates` folder, we will create two HTML files. These files will form the basis of our application's user interface.

```bash
# Navigate into the templates directory
cd templates

# Create home.html and todo.html
touch home.html todo.html
```

We have now created two essential template files:

  * `home.html`: This will serve as our **base template** or main layout. It will contain the common structure of our application, like the header and footer.
  * `todo.html`: This will be a **child template** that contains the specific content for the to-do list and form. It will inherit the structure from `home.html`.

In the mockup shown earlier, you can think of `home.html` as the outer box (the overall page structure) and `todo.html` as the inner box (the main content area).

-----

### 3\. Configuring Jinja within the FastAPI Application ⚙️

Now, we need to update our Python code to make FastAPI aware of our templates and instruct it to render HTML instead of JSON. This involves changes in both `todo.py` and `model.py`.

#### A. Updating the API Routes in `todo.py`

Let's modify our route handlers to return HTML responses.

```python
from fastapi import APIRouter, Path, HTTPException, status, Request, Depends
from fastapi.templating import Jinja2Templates
from model import Todo, TodoItem, TodoItems

todo_router = APIRouter()
todo_list = []

# Create an instance of Jinja2Templates and point it to the "templates" directory
templates = Jinja2Templates(directory="templates/")

@todo_router.post("/todo")
async def add_todo(request: Request, todo: Todo = Depends(Todo.as_form)):
    todo.id = len(todo_list) + 1
    todo_list.append(todo)
    
    # Return a TemplateResponse instead of JSON
    return templates.TemplateResponse("todo.html", {
        "request": request,
        "todos": todo_list
    })

@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todo(request: Request):
    # Return a TemplateResponse with the list of todos
    return templates.TemplateResponse("todo.html", {
        "request": request,
        "todos": todo_list
    })

@todo_router.get("/todo/{todo_id}")
async def get_single_todo(request: Request, todo_id: int = Path(..., title="The ID of the todo to retrieve.")):
    for todo in todo_list:
        if todo.id == todo_id:
            # Return a TemplateResponse with the single todo item
            return templates.TemplateResponse("todo.html", {
                "request": request,
                "todo": todo
            })
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist",
    )
```

#### Code Explanation 🧐

  * **`from fastapi.templating import Jinja2Templates`**: We import the class required to work with Jinja2 templates.
  * **`templates = Jinja2Templates(directory="templates/")`**: This line is crucial. It creates an instance of `Jinja2Templates` and tells it that our template files are located in the `templates/` directory.
  * **`request: Request`**: Each route that renders a template now requires the `Request` object as a parameter. This is mandatory for the `TemplateResponse`.
  * **`return templates.TemplateResponse(...)`**: This is the most significant change. Instead of returning a Python dictionary (which FastAPI automatically converts to JSON), we now return a `TemplateResponse`. This object takes two arguments:
    1.  The **name of the template file** to render (e.g., `"todo.html"`).
    2.  A **context dictionary** containing the data to be passed to the template. The `"request": request` key-value pair is required. Other keys, like `"todos": todo_list`, pass our application data to the template, making it available for display.
  * **`Depends(Todo.as_form)`**: The `POST` route now uses a dependency to process incoming data as an HTML form submission rather than a JSON payload. We'll define this dependency next.

#### B. Updating the Pydantic Model in `model.py`

To handle HTML form submissions, we need to add a class method to our `Todo` model.

```python
from typing import List, Optional
from pydantic import BaseModel
from fastapi import Form

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
```

#### Code Explanation 🧐

  * **`@classmethod def as_form(...)`**: We've added a special class method called `as_form`. This method allows our Pydantic model to be populated from incoming HTML form data instead of a JSON body. The `item: str = Form(...)` part tells FastAPI to extract the `item` value from the form data.

-----

### 4\. Crafting the Base Template: `home.html` 🏛️

Now let's write the HTML for our base template. This file defines the overall page layout.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta content="IE=edge" http-equiv="X-UA-Compatible">
    <meta content="width=device-width, initial-scale=1.0" name="viewport">
    <title>Packt Todo Application</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <link crossorigin="anonymous" href="https://use.fontawesome.com/releases/v5.0.10/css/all.css"
          integrity="sha384-+d0P83n9kaQMCwj8F4RJB66tzIwOKmrdb46+porD/OvrJ+37WqIM7UoBtwHO6Nlg" rel="stylesheet">
</head>
<body>
<header>
    <nav class="navbar bg-body-tertiary">
        <div class="container-fluid">
            <center>
                <h1>Todo Application</h1>
            </center>
        </div>
    </nav>
</header>
<div class="container-fluid">
    {% block todo_container %}{% endblock %}
</div>
</body>
</html>
```

#### Code Explanation 🧐

  * **`{% block todo_container %}{% endblock %}`**: This is the core of Jinja's template inheritance. This `block` tag defines a section named `todo_container`. It acts as a placeholder. A child template can "fill in" this block with its own specific content.

-----

### 5\. Running the Application and First Preview 🌐

Let's see our base template in action. Start your application from the terminal.

```bash
# Make sure your virtual environment is active
$ source venv/bin/activate

# Start the Uvicorn server
uvicorn api:app --host=0.0.0.0 --port 8000 --reload
```

Now, open your web browser and navigate to **`http://127.0.0.1:8000/todo`**. You should see the basic page layout with the header but no to-do list yet.

-----

### 6\. Creating the Child Template: `todo.html` 🧩

Next, let's write the content for `todo.html`. This template will extend our base layout and provide the form for adding to-dos and the list for displaying them.

```jinja
{% extends "home.html" %}

{% block todo_container %}
<main class="container">
    <hr>
    <section class="container-fluid">
        <form method="post">
            <div class="col-auto">
                <div class="input-group mb-3">
                    <input aria-describedby="button-addon2" aria-label="Add a todo" class="form-control" name="item"
                           placeholder="Purchase Packt's Python workshop course" type="text"
                           value="{{ item }}"/>
                    <button class="btn btn-outline-primary" data-mdb-ripple-color="dark" id="button-addon2"
                            type="submit">
                        Add Todo
                    </button>
                </div>
            </div>
        </form>
    </section>

    {% if todo %}
    <article class="card container-fluid">
        <br/>
        <h4>Todo ID: {{ todo.id }} </h4>
        <p>
            <strong>
                Item: {{ todo.item }}
            </strong>
        </p>
    </article>
    {% else %}
    <section class="container-fluid">
        <h2 align="center">Todos</h2>
        <br>
        <div class="card">
            <ul class="list-group list-group-flush">
                {% for todo in todos %}
                <li class="list-group-item">
                    {{ loop.index }}. <a href="/todo/{{ todo.id }}"> {{ todo.item }} </a>
                </li>
                {% endfor %}
            </ul>
        </div>
    </section>
    {% endif %}
</main>
{% endblock %}
```

#### Code Explanation 🧐

  * **`{% extends "home.html" %}`**: This line must be the very first thing in the file. It tells Jinja that this template inherits from `home.html`.
  * **`{% block todo_container %}`**: All the content inside this block will be injected into the `todo_container` placeholder in `home.html`.
  * **`{% if todo %}` ... `{% else %}` ... `{% endif %}`**: This is conditional logic. The template checks if a single `todo` variable was passed in the context.
      * If **yes** (when viewing `/todo/{todo_id}`), it displays the details of that single to-do.
      * If **no** (when viewing `/todo`), it renders the `else` block, which contains the list of all to-dos.
  * **`{% for todo in todos %}` ... `{% endfor %}`**: This loop iterates through the `todos` list passed from our FastAPI endpoint and creates a list item (`<li>`) for each one.
  * **`{{ loop.index }}` and `{{ todo.item }}`**: These are Jinja expressions that print data. `loop.index` is a special loop variable that gives the current iteration number (starting from 1), and `todo.item` accesses the `item` attribute of the current `todo` object in the loop. The link `<a href="/todo/{{ todo.id }}">` is created dynamically.

-----

### 7\. Final Verification: A Complete Walkthrough ✅

Now, refresh your browser at `http://127.0.0.1:8000/todo`. You should see the complete application interface, including the form and the (currently empty) to-do list.

**1. Add a new to-do:** Type a task into the input field and click "Add Todo." The page should refresh, and your new to-do will appear in the list.

**2. View a single to-do:** The to-do item in the list is a clickable link. Click on it.

You will be taken to a new page showing only the details of that specific to-do, demonstrating that the `{% if todo %}` logic in our template is working correctly.


---
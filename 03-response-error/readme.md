# 🚀 **Understanding Responses in FastAPI**

Responses are a fundamental part of how an API operates. They represent the feedback you receive after interacting with an API endpoint using any of the standard HTTP methods. Typically, an API response is formatted in JSON or XML, but it can also be a document.

Every response is composed of two primary parts: a **header** and a **body**.

---

### What is a Response Header? 📨

The **response header** contains the status of the original request along with additional metadata to guide the delivery of the response body. A common example of information found in the header is the `Content-Type`, which informs the client about the type of content being returned (e.g., `application/json`).

### What is a Response Body? 📦

The **response body** is the actual data that the client requested from the server. The format of this data is determined by the `Content-Type` specified in the header. For instance, the list of to-dos returned in the previous examples constitutes the response body.

Now that we have a clear understanding of what responses are, let's explore the HTTP status codes that are included within them.

---

## 🚦 Decoding HTTP Status Codes

**Status codes** are unique, short codes issued by a server in response to a client's request. These codes are grouped into five distinct categories, each signifying a different type of response outcome.

### Categories of Status Codes

* **`1XX`**: Informational - The request has been received and the process is continuing.
* **`2XX`**: Success - The request was successfully received, understood, and accepted.
* **`3XX`**: Redirection - Further action needs to be taken to complete the request.
* **`4XX`**: Client Error - The request contains bad syntax or cannot be fulfilled.
* **`5XX`**: Server Error - The server failed to fulfill an apparently valid request.

The first digit of a status code defines its category. Common examples include `200` for a successful request, `404` when a resource is not found, and `500` for an internal server error.

A standard practice in web development, regardless of the framework, is to return the appropriate status code for each specific event. For example, a `400` status code should not be returned for a server-side error, and a `200` status code should not be returned for a failed operation.

### `1XX` Informational Responses ℹ️

| Code | Meaning | SEO / Use Case |
| :--- | :--- | :--- |
| **100** | Continue | Request received, the client should proceed with the request. Rarely used in SEO. |
| **101** | Switching Protocols | The server is switching protocols as requested by the client. Has no SEO impact. |
| **102** | Processing | The server has received and is processing the request, but no response is available yet. Used for long operations (e.g., WebDAV); has no SEO impact. |

### `2XX` Success ✅

| Code | Meaning | SEO / Use Case |
| :--- | :--- | :--- |
| **200** | OK | The request succeeded. This is the standard response crawlers look for. |
| **201** | Created | A new resource was successfully created (often after a `POST` request). Used for API success confirmation; not directly related to crawling. |
| **202** | Accepted | The request has been received but not yet acted upon. Used for asynchronous operations; has no SEO effect. |
| **203** | Non-Authoritative Information | The response is from a transforming proxy. Rare and provides no SEO value. |
| **204** | No Content | The request was successful, but there is no response body to return. Useful for APIs. |
| **205** | Reset Content | Instructs the client to reset the document view (e.g., clear a form). Not relevant to SEO. |
| **206** | Partial Content | The server delivered only part of the resource. Used for large files or media streaming; not for SEO purposes. |
| **207** | Multi-Status | Provides status for multiple independent operations (WebDAV). Not relevant to SEO. |
| **208** | Already Reported | Used inside a DAV `propstat` response element to avoid enumerating the internal members of multiple bindings to the same collection repeatedly. A WebDAV code; not relevant to SEO. |
| **226** | IM Used | The server has fulfilled a `GET` request for the resource, and the response is a representation of the result of one or more instance-manipulations applied to the current instance. Rare; not related to SEO. |

### `3XX` Redirection ↪️

| Code | Meaning | SEO / Use Case |
| :--- | :--- | :--- |
| **300** | Multiple Choices | The request has more than one possible response. May confuse crawlers; should be avoided. |
| **301** | Moved Permanently | The resource has been permanently moved to a new URL. This is the most SEO-friendly redirect. |
| **302** | Found | The resource is temporarily at a different URI. Avoid for long-term SEO; use a `301` instead. |
| **303** | See Other | Directs the client to get the requested resource at another URI with a `GET` request. Often used after form submissions. |
| **304** | Not Modified | The client can use its cached version of the response. This helps reduce crawl load. |
| **305** | Use Proxy | The requested resource must be accessed through a proxy. Deprecated and should be ignored. |
| **307** | Temporary Redirect | Same as `302`, but the request method is not allowed to be changed. For temporary moves; no long-term SEO benefit. |
| **308** | Permanent Redirect | Same as `301`, but the request method is not allowed to be changed. A good SEO alternative to `301`. |

### `4XX` Client Error ❌

| Code | Meaning | SEO / Use Case |
| :--- | :--- | :--- |
| **400** | Bad Request | The server could not understand the request due to invalid syntax. Check logs to fix malformed URLs. |
| **401** | Unauthorized | Authentication is required to access the resource. May unintentionally block crawlers. |
| **402** | Payment Required | Reserved for future use. Not relevant to SEO. |
| **403** | Forbidden | The server understood the request but refuses to authorize it. Ensure important pages are not restricted. |
| **404** | Not Found | The server cannot find the requested resource. Customize the page or implement redirects. |
| **405** | Method Not Allowed | The request method is not supported for the requested resource. Rare; check API endpoint configurations. |
| **406** | Not Acceptable | The server cannot produce a response matching the list of acceptable values defined in the request's proactive content negotiation headers. Rare; not SEO-focused. |
| **407** | Proxy Authentication Required | The client must first authenticate itself with the proxy. Not relevant to SEO. |
| **408** | Request Timeout | The server timed out waiting for the request. Could disrupt crawlers. |
| **409** | Conflict | The request conflicts with the current state of the server (e.g., edit conflicts). Used in web apps; not for SEO. |
| **410** | Gone | The requested resource is intentionally and permanently removed. Informs search engines that the page is gone. |
| **411** | Length Required | The server rejected the request because the `Content-Length` header field is not defined and the server requires it. Rare; not relevant to SEO. |
| **412** | Precondition Failed | The client has indicated preconditions in its headers which the server does not meet. Used for APIs/WebDAV. |
| **413** | Payload Too Large | The request entity is larger than the limits defined by the server. Rare; no SEO impact. |
| **414** | Request-URI Too Long | The URI requested by the client is longer than the server is willing to interpret. Avoid overly long URLs for SEO. |
| **415** | Unsupported Media Type | The media format of the requested data is not supported by the server. No SEO impact. |
| **416** | Requested Range Not Satisfiable | The range specified by the `Range` header field in the request cannot be fulfilled. No SEO impact. |
| **417** | Expectation Failed | The expectation given in the `Expect` request-header field could not be met by the server. Rare. |
| **418** | I'm a Teapot | A joke code from RFC 2324. No use case. |
| **421** | Misdirected Request | The request was directed at a server that is not able to produce a response. Can be caused by CDN issues. |
| **422** | Unprocessable Entity | The request was well-formed but was unable to be followed due to semantic errors. Used in WebDAV; not for SEO. |
| **423** | Locked | The resource that is being accessed is locked. Used in WebDAV. |
| **424** | Failed Dependency | The request failed due to the failure of a previous request. Used in WebDAV. |
| **426** | Upgrade Required | The server refuses to perform the request using the current protocol but might be willing to do so after the client upgrades to a different protocol. Not relevant to SEO. |
| **428** | Precondition Required | The origin server requires the request to be conditional. Rare. |
| **429** | Too Many Requests | The user has sent too many requests in a given amount of time ("rate limiting"). May block bots. |
| **431** | Request Header Fields Too Large | The server is unwilling to process the request because its header fields are too large. Could block crawlers. |
| **444** | Connection Closed Without Response | An Nginx-specific code indicating the server has dropped the connection without sending a response. Used to terminate unwanted requests. Treat as a network error; audit firewall rules. |
| **451** | Unavailable For Legal Reasons | The server is denying access to the resource as a consequence of a legal demand. May cause content to be de-indexed from search results. |
| **499** | Client Closed Request | An Nginx-specific code indicating the client closed the connection before the server could send a response. Investigate long server response times (TTFB) and network instability. |

### `5XX` Server Error 🖥️

| Code | Meaning | SEO / Use Case |
| :--- | :--- | :--- |
| **500** | Internal Server Error | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. Must be fixed immediately as it harms SEO. |
| **501** | Not Implemented | The server does not have the functionality to fulfill the request. Rare. |
| **502** | Bad Gateway | The server, while acting as a gateway or proxy, received an invalid response from an upstream server. Check hosting/CDN configurations. |
| **503** | Service Unavailable | The server is not ready to handle the request (e.g., overloaded or down for maintenance). Use for planned downtime. |
| **504** | Gateway Timeout | The server, while acting as a gateway or proxy, did not get a response in time from the upstream server. Indicates hosting/CDN issues. |
| **505** | HTTP Version Not Supported | The HTTP version used in the request is not supported by the server. Rare. |
| **506** | Variant Also Negotiates | There is a configuration error in the server's content negotiation. Rare. |
| **507** | Insufficient Storage | The method could not be performed on the resource because the server is unable to store the representation needed to successfully complete the request (WebDAV). Not relevant to SEO. |
| **508** | Loop Detected | The server detected an infinite loop while processing the request (WebDAV). |
| **510** | Not Extended | Further extensions to the request are required for the server to fulfill it. Rare. |
| **511** | Network Authentication Required | The client needs to authenticate to gain network access. No SEO impact. |
| **599** | Network Connect Timeout Error | A network timeout error not covered by `504`. Used by some CDNs and proxies like HAProxy. Signals upstream instability. Monitor hosting/CDN for issues. |


---

# 🏗️ **Building Response Models in FastAPI**

In FastAPI, **response models** are a powerful feature for defining the precise data structure of the output an API endpoint should return. While they are built using Pydantic, just like input models, their primary purpose is to shape, filter, and validate the outgoing data.

-----

### The Challenge: Unfiltered API Responses  unfiltered

Let's consider a simple API route designed to retrieve a list of to-do items from a database or an in-memory list.

#### Example Route Definition

Without a response model, the route might look like this:

```python
@todo_router.get("/todo")
async def retrieve_todo() -> dict:
    return {"todos": todo_list}
```

This endpoint is defined to return a dictionary. If `todo_list` contains objects with multiple fields (e.g., `id` and `item`), the API will return all of them.

#### Example Output

A request to this endpoint would yield the following JSON response, which includes every field for each to-do item:

```json
{
  "todos": [
    {
      "id": 1,
      "item": "IGI ORIGIN"
    },
    {
      "id": 2,
      "item": "Call Of Duty Ghost"
    },
    {
      "id": 3,
      "item": "Call Of Duty Modern Warfare"
    }
  ]
}
```

To return only specific information, such as just the to-do item descriptions, one would typically need to write additional logic to process and filter the data before sending it. Fortunately, FastAPI provides a more elegant solution using the `response_model` argument.

-----

### The Solution: Crafting Pydantic Models for Output ✨

We can create specific Pydantic models that declare exactly which fields should be included in the response. Let's create two new models in the `model.py` file to structure our desired output. Our goal is to return an array of just the to-do items, excluding their IDs.

#### Code: `model.py`

```python
from pydantic import BaseModel
from typing import List

# Defines the structure for a single to-do item in the response.
class TodoItem(BaseModel):
    item: str

    # Provides example data for the API documentation.
    class Config:
        json_schema_extra = {
            "example": {
                "item": "Read the next chapter of the book"
            }
        }

# Defines the structure for the top-level response object.
class TodoItems(BaseModel):
    todos: List[TodoItem]

    # Provides a full example for the list of items.
    class Config:
        json_schema_extra = {
            "example": {
                "todos": [
                    {"item": "Example schema 1!"},
                    {"item": "Example schema 2!"},
                    {"item": "Example schema 3!"}
                ]
            }
        }
```

#### Code Explanation 🧐

  * **`TodoItem(BaseModel)`**: This class defines the structure for a *single* item in our response list.

      * `item: str`: It declares that each to-do object in the response must have a field named `item` which is a string.
      * `class Config`: This nested class is used to configure the model's behavior.
      * `json_schema_extra`: This dictionary provides example data that will be displayed in the automatically generated API documentation (like Swagger UI), making the API easier to understand and use.

  * **`TodoItems(BaseModel)`**: This class defines the overall structure of the final JSON response.

      * `todos: List[TodoItem]`: This is the key part. It declares a field named `todos` that must be a list (`List`) where each element in the list conforms to the `TodoItem` model we just defined. This creates a nested model structure.

-----

### Applying the Response Model to the Route ⚙️

Now, let's update our route in `todo.py` to use the newly created `TodoItems` model as its response model.

#### Code: `todo.py`

```python
# Import the new models along with the existing Todo model.
from model import Todo, TodoItem, TodoItems
...

@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todo() -> dict:
    return {"todos": todo_list}
```

#### Code Explanation 🧐

  * `from model import Todo, TodoItem, TodoItems`: We first import the necessary models.
  * `response_model=TodoItems`: This is the crucial addition to the route decorator. By setting this argument, we instruct FastAPI to:
    1.  **Filter the Output**: Automatically process the data returned by the function (`{"todos": todo_list}`) and ensure the final JSON response matches the structure of the `TodoItems` model. Any fields not defined in `TodoItems` (like `id`) will be excluded.
    2.  **Validate Data**: Ensure the returned data is of the correct type.
    3.  **Document the API**: Update the API documentation to show clients exactly what the response schema will look like.

-----

### Putting It All Together: A Practical Demonstration 🧪

Let's start the application and test the updated endpoint.

#### 1\. Start the Application

Run the following command in your terminal to start the Uvicorn server:

```bash
uvicorn api:app --host=0.0.0.0 --port 8000 --reload
```

#### 2\. Populate Data with `POST` Requests

Before we can retrieve data, let's add a few to-do items using `POST` requests. We'll use `curl` for this.

**Add Item 1:**

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/todo' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 1,
  "item": "IGI ORIGIN"
}'
```

*Response:* `{"message":"Todo added successfully","todo":{"id":1,"item":"IGI ORIGIN"}}`

**Add Item 2:**

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/todo' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 2,
  "item": "Call Of Duty Ghost"
}'
```

*Response:* `{"message":"Todo added successfully","todo":{"id":2,"item":"Call Of Duty Ghost"}}`

**Add Item 3:**

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/todo' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 3,
  "item": "Call Of Duty Modern Warfare"
}'
```

*Response:* `{"message":"Todo added successfully","todo":{"id":3,"item":"Call Of Duty Modern Warfare"}}`

#### 3\. Retrieve Filtered Data with a `GET` Request

Now, let's call our updated `GET` endpoint to retrieve all the to-dos.

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/todo' \
  -H 'accept: application/json'
```

-----

### Analyzing the Final Output ✅

After running the `GET` request, the API returns the following JSON. Notice how FastAPI has automatically filtered the output to match our `TodoItems` response model.

```json
{
  "todos": [
    {
      "item": "IGI ORIGIN"
    },
    {
      "item": "Call Of Duty Ghost"
    },
    {
      "item": "Call Of Duty Modern Warfare"
    }
  ]
}
```

As you can see, the `id` field is no longer present in the response. The output perfectly conforms to the structure we defined, demonstrating the power and convenience of using response models to shape your API's output without writing extra filtering logic.


---

# 🚨 **Proper Error Handling in FastAPI**

Handling errors correctly is crucial for building robust and user-friendly APIs. When requests fail, the responses should be clear and informative, not ugly or confusing. Errors can occur for many reasons, such as attempting to access a resource that doesn't exist, lacking the necessary permissions for a protected page, or encountering an internal server issue.

In FastAPI, the standard way to handle these situations is by raising an `HTTPException`.

-----

## What is an `HTTPException`? 🌋

An **HTTPException** is a special exception class provided by FastAPI. You can raise it at any point in your code to immediately stop the processing of a request and send a well-formatted HTTP error response to the client.

The `HTTPException` class accepts three main arguments:

  * **`status_code`**: The HTTP status code you want to return (e.g., `404`, `403`).
  * **`detail`**: A clear, descriptive message to be sent in the response body, explaining the error.
  * **`headers`**: An optional dictionary of any custom headers you need to include in the error response. For example, `{"X-Error": "Resource Not Found"}` adds a custom `X-Error` header to the response.

-----

## The Problem: Returning Incorrect Status Codes ⚠️

In our current to-do application, if we try to retrieve a to-do item with an ID that doesn't exist, the API returns a success message with a `200 OK` status code. This is misleading because the operation actually failed. The correct behavior would be to return a `404 Not Found` status code.

By updating our routes to use `HTTPException`, we can return the correct status code along with relevant details in the response.

-----

## The Solution: Raising `HTTPException` for Accurate Responses ✅

Let's modify the routes responsible for retrieving, updating, and deleting a single to-do item in the `todo.py` file to incorporate `HTTPException`. We will add a custom header to the "get single todo" route as an example.

#### Code: `todo.py`

```python
from fastapi import APIRouter, Path, HTTPException, status
# ... other code

@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="The ID of the todo to retrieve.")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo": todo
            }
    # If the loop finishes without finding the todo, raise an exception.
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist",
        headers={"X-Error": "There was an error finding this todo"},
    )

@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., title="The ID of the todo to be updated.")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {
                "message": "Todo updated successfully."
            }
    # If the todo is not found, raise an exception.
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist",
    )

@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {
                "message": "Todo deleted successfully."
            }
    # If the todo is not found, raise an exception.
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist",
    )
```

#### Code Explanation 🧐

  * **Import `HTTPException` and `status`**: We start by importing the necessary components from FastAPI. The `status` module provides convenient access to standard HTTP status codes, making the code more readable.
  * **Updated Logic**: In each of the three routes, the logic is modified. If the `for` loop completes without finding a matching `todo_id`, it means the requested to-do does not exist.
  * **`raise HTTPException(...)`**: Instead of returning a success message, the code now raises an `HTTPException`, which immediately sends an error response to the client.
  * **Custom Headers Example**: In the `get_single_todo` route, we've added the `headers` argument:
      * `headers={"X-Error": "There was an error finding this todo"}`: This dictionary adds a custom `X-Error` HTTP header to the `404 Not Found` response. This is useful for providing additional, machine-readable context about the error.

-----

### Verifying the Fix 🔬

Now, if we retry the request for a non-existent to-do item, our API documentation will show the correct `404 Not Found` response. If we inspect the response headers using developer tools or a tool like `curl -v`, we would also see our custom `X-Error` header.

-----

## Customizing Success Status Codes 🎉

Just as we can control error codes, FastAPI also allows us to override the default status code for successful operations. By default, a successful request returns a `200 OK`. However, for operations that create a new resource (like a `POST` request), the conventional status code is `201 Created`.

We can specify this by adding the `status_code` argument to the route decorator.

#### Code: `todo.py`

```python
@todo_router.post("/todo", status_code=201)
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {
        "message": "Todo added successfully."
    }
```

#### Code Explanation 🧐

  * **`status_code=201`**: By adding this argument to the `@todo_router.post()` decorator, we are telling FastAPI that when this endpoint executes successfully, it should return an HTTP status of `201 Created` instead of the default `200 OK`.

This section has shown how to return appropriate response codes for both errors and successful operations, a key practice in building professional and predictable APIs.


---
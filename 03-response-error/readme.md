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